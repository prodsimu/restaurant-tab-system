from app.api.v1.schemas.item_schema import ItemCreateSchema, ItemUpdateSchema
from app.domain.entities.item_entity import ItemCreateEntity
from app.domain.exceptions.item_exceptions import ItemNotFoundError
from app.domain.exceptions.product_exceptions import ProductNotFoundError
from app.domain.exceptions.tab_exceptions import TabNotFoundError
from app.infrastructure.database.models.item_model import ItemModel
from app.infrastructure.database.unit_of_work import UnitOfWork


class ItemService:

    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    # CREATE

    def add_item_to_tab(self, data: ItemCreateSchema) -> ItemModel:
        with self.uow as uow:
            tab = uow.tabs.get_open_tab_by_number(data.tab_number)

            if not tab:
                raise TabNotFoundError("Tab is not open")

            product = uow.products.get_product_by_id(data.product_id)

            if not product:
                raise ProductNotFoundError("Product not found")

            entity = ItemCreateEntity(tab.id, data.product_id, data.quantity)

            item = uow.items.get_item_by_tab_and_product(
                entity.tab_id, entity.product_id
            )

            if item:
                return uow.items.increment_quantity(item, entity.quantity)

            return uow.items.create_item(
                tab_id=entity.tab_id,
                product_id=entity.product_id,
                quantity=entity.quantity,
            )

    # READ

    def list_tab_items(self, tab_number: int) -> list[ItemModel]:
        with self.uow as uow:
            tab = uow.tabs.get_open_tab_by_number(tab_number)

            if not tab:
                raise TabNotFoundError("Tab is not open")

            return uow.items.list_items_by_tab(tab.id)

    # UPDATE

    def decrement_item_quantity(
        self, item_id: int, data: ItemUpdateSchema
    ) -> ItemModel | dict:
        with self.uow as uow:
            item = uow.items.get_item_by_id(item_id)

            if not item:
                raise ItemNotFoundError(f"Item with ID {item_id} not found")

            result = uow.items.decrement_quantity(item, data.quantity)

        if result is None:
            return {"message": f"Item with ID {item_id} deleted successfully"}

        return result

    # DELETE

    def delete_item_from_tab(self, item_id: int) -> dict:
        with self.uow as uow:
            item = uow.items.get_item_by_id(item_id)

            if not item:
                raise ItemNotFoundError(f"Item with ID {item_id} not found")

            uow.items.delete_item(item)

        return {"message": f"Item with ID {item_id} deleted successfully"}
