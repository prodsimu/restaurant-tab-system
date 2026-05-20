from datetime import datetime, timezone

from sqlalchemy import and_
from sqlalchemy.orm import Session

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
    def open_tab_by_number(db: Session, number: int) -> TabModel:

        tab = (
            db.query(TabModel)
            .filter(and_(TabModel.number == number, TabModel.is_open))
            .first()
        )

        if tab:
            raise TabAlreadyOpenError(
                f"An open tab with number {number} already exists."
            )

        entity = TabCreateEntity(number, True, datetime.now(timezone.utc), None)

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
    def list_tabs_by_number(db: Session, number: int) -> TabModel:
        tabs = db.query(TabModel).filter(TabModel.number == number).all()

        if not tabs:
            raise TabNotFoundError(f"Tabs with number {number} not found.")

        return tabs

    # UPDATE

    @staticmethod
    def close_tab_by_number(db: Session, number: int) -> TabModel:

        tab = (
            db.query(TabModel)
            .filter(and_(TabModel.number == number, TabModel.is_open))
            .first()
        )

        if not tab:
            raise TabAlreadyClosedError(f"No open tab with number {number} exists.")

        tab.is_open = False
        tab.closed_at = datetime.now(timezone.utc)

        db.commit()
        db.refresh(tab)

        return tab

    # DELETE

    @staticmethod
    def delete_tab_by_id(db: Session, id: int) -> dict:

        tab = db.query(TabModel).filter(and_(TabModel.id == id)).first()

        if not tab:
            raise TabNotFoundError(f"Tab with ID {id} not found.")

        db.delete(tab)
        db.commit()

        return {"message": f"Tab with ID {id} deleted successfully"}
