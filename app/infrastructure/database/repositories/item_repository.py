from sqlalchemy.orm import Session

from app.domain.repositories.item_repository import ItemRepositoryInterface
from app.infrastructure.database.models.item_model import ItemModel


class ItemRepository(ItemRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db
