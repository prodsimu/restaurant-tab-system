from sqlalchemy.orm import Session

from app.domain.repositories.item_repository import ItemRepositoryInterface
from app.infrastructure.database.models.item_model import ItemModel


class ItemRepository(ItemRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db

    # CREATE

    def create_item(self, tab_id: int, product_id: int, quantity: int) -> ItemModel:
        db_model = ItemModel(tab_id=tab_id, product_id=product_id, quantity=quantity)

        self.db.add(db_model)
        self.db.commit()
        self.db.refresh(db_model)

        return db_model
