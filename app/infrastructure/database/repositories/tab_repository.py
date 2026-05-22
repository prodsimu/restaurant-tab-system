from sqlalchemy.orm import Session

from app.domain.repositories.tab_repository import TabRepositoryInterface
from app.infrastructure.database.models.tab_model import TabModel


class TabRepository(TabRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db

    def get_open_tab_by_number(self, tab_number: int) -> TabModel:
        return (
            self.db.query(TabModel)
            .filter(TabModel.number == tab_number, TabModel.is_open)
            .first()
        )
