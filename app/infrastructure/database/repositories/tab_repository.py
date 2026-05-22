from sqlalchemy.orm import Session

from app.domain.repositories.tab_repository import TabRepositoryInterface
from app.infrastructure.database.models.tab_model import TabModel


class TabRepository(TabRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db
