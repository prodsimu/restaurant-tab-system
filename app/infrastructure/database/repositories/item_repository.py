from sqlalchemy import and_
from sqlalchemy.orm import Session

from app.domain.repositories.item_repository import ItemRepositoryInterface
from app.infrastructure.database.models.item_model import ItemModel


class ItemRepository(ItemRepositoryInterface):

    def __init__(self, db: Session):
        self.db = db

    # CREATE

    def create_item(self, tab_id: int, product_id: int, quantity: int) -> ItemModel:
        item = ItemModel(
            tab_id=tab_id,
            product_id=product_id,
            quantity=quantity,
        )
        self.db.add(item)
        self.db.flush()
        self.db.refresh(item)
        return item

    # READ

    def get_item_by_id(self, item_id: int) -> ItemModel | None:
        return self.db.query(ItemModel).filter(ItemModel.id == item_id).first()

    def get_item_by_tab_and_product(
        self, tab_id: int, product_id: int
    ) -> ItemModel | None:
        return (
            self.db.query(ItemModel)
            .filter(
                and_(
                    ItemModel.tab_id == tab_id,
                    ItemModel.product_id == product_id,
                )
            )
            .first()
        )

    def list_items_by_tab(self, tab_id: int) -> list[ItemModel]:
        return self.db.query(ItemModel).filter(ItemModel.tab_id == tab_id).all()

    # UPDATE

    def increment_quantity(self, item: ItemModel, quantity: int) -> ItemModel:
        item.quantity += quantity
        self.db.flush()
        self.db.refresh(item)
        return item

    def decrement_quantity(self, item: ItemModel, quantity: int) -> ItemModel | None:
        item.quantity -= quantity

        if item.quantity <= 0:
            self.db.delete(item)
            self.db.flush()
            return None

        self.db.flush()
        self.db.refresh(item)
        return item

    # DELETE

    def delete_item(self, item: ItemModel) -> None:
        self.db.delete(item)
        self.db.flush()
