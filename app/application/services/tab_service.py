from datetime import datetime, timezone

from sqlalchemy import and_
from sqlalchemy.orm import Session

from app.api.v1.schemas.tab_schema import TabCreateSchema
from app.domain.entities.tab_entity import TabCreateEntity
from app.domain.exceptions.tab_exceptions import (
    TabAlreadyClosedError,
    TabAlreadyOpenError,
    TabNotFoundError,
)
from app.infrastructure.database.models.tab_model import TabModel


class TabService:

    # CREATE

    @staticmethod
    def open_tab_by_number(db: Session, data: TabCreateSchema):

        existing_tabs = db.query(TabModel).filter(TabModel.number == data.number).all()

        for tab in existing_tabs:
            if tab.is_open:
                raise TabAlreadyOpenError(
                    "An open tab with this number already exists."
                )

        entity = TabCreateEntity(
            data.number, data.is_open, data.created_at, data.closed_at
        )

        entity.validate()

        db_model = TabModel(
            number=entity.number,
            is_open=entity.is_open,
            created_at=entity.created_at,
            closed_at=entity.closed_at,
        )

        db.add(db_model)
        db.commit()
        db.refresh(db_model)

        return db_model

    # READ

    @staticmethod
    def get_tab_by_number(db: Session, number: int) -> TabModel:
        tab = db.query(TabModel).filter(TabModel.number == number).first()

        if not tab:
            raise TabNotFoundError("Tab not found.")

        return tab

    # UPDATE

    @staticmethod
    def close_tab_by_number(db: Session, number: int) -> TabModel:

        tab = (
            db.query(TabModel)
            .filter(and_(TabModel.number == number, TabModel.is_open))
            .first()
        )

        if not tab:
            raise TabAlreadyClosedError("No open tab with this number exists.")

        tab.is_open = False
        tab.closed_at = datetime.now(timezone.utc)

        db.commit()
        db.refresh(tab)

        return tab

    # DELETE

    @staticmethod
    def delete_tab_by_number(db: Session, number: int) -> TabModel:

        tab = TabService.get_tab_by_number(db, number)

        db.delete(tab)
        db.commit()

        return tab
