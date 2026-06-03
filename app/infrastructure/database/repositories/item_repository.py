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

    # READ

    def get_item_by_id(self, item_id: int) -> ItemModel:
        return self.db.query(ItemModel).filter(ItemModel.id == item_id).first()

    def list_items_by_tab_id(self, tab_id: int) -> list[ItemModel]:
        return self.db.query(ItemModel).filter(ItemModel.tab_id == tab_id).all()

    # UPDATE

    def increment_quantity(self, item_id: int, quantity: int) -> ItemModel:
        item = self.get_item_by_id(item_id)
        item.quantity += quantity

        self.db.commit()
        self.db.refresh(item)

        return item

    def decrement_quantity(self, item_id: int, quantity: int) -> ItemModel:
        item = self.get_item_by_id(item_id)
        item.quantity -= quantity

        self.db.commit()
        self.db.refresh(item)

        return item
