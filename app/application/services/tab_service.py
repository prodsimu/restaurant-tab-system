from sqlalchemy.orm import Session

from app.domain.exceptions.tab_exceptions import TabNotFoundError
from app.infrastructure.database.models.tab_model import TabModel


class TabService:

    # CREATE

    # READ

    @staticmethod
    def get_tab_by_number(db: Session, number: int) -> TabModel:
        tab = db.query(TabModel).filter(TabModel.number == number).first()

        if not tab:
            raise TabNotFoundError("User not found.")

        return tab

    # UPDATE

    # DELETE
