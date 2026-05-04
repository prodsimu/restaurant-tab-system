from sqlalchemy.orm import Session

from app.api.v1.schemas.tab_schema import TabCreateSchema
from app.domain.entities.tab_entity import TabCreateEntity
from app.domain.exceptions.tab_exceptions import TabAlreadyExistsError, TabNotFoundError
from app.infrastructure.database.models.tab_model import TabModel


class TabService:

    # CREATE

    @staticmethod
    def create_tab(db: Session, data: TabCreateSchema):

        try:
            TabService.get_tab_by_number(db, data.number)
            raise TabAlreadyExistsError(f"Tab {data.number} already exists.")

        except TabNotFoundError:
            pass

        entity = TabCreateEntity(data.number, data.is_empty)

        entity.validate()

        db_model = TabModel(number=entity.number, is_empty=entity.is_empty)

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

    # DELETE

    @staticmethod
    def delete_tab_by_number(db: Session, number: int) -> TabModel:

        tab = TabService.get_tab_by_number(db, number)

        db.delete(tab)
        db.commit()

        return tab
