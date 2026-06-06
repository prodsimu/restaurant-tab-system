from abc import ABC, abstractmethod

from app.infrastructure.database.models.item_model import ItemModel


class ItemRepositoryInterface(ABC):

    # CREATE

    @abstractmethod
    def create_item(self, tab_id: int, product_id: int, quantity: int) -> ItemModel: ...

    # READ

    @abstractmethod
    def get_item_by_id(self, item_id: int) -> ItemModel | None: ...

    @abstractmethod
    def get_item_by_tab_and_product(
        self, tab_id: int, product_id: int
    ) -> ItemModel | None: ...

    @abstractmethod
    def list_items_by_tab(self, tab_id: int) -> list[ItemModel]: ...

    # UPDATE

    @abstractmethod
    def increment_quantity(self, item: ItemModel, quantity: int) -> ItemModel: ...

    # DELETE

    @abstractmethod
    def delete_item(self, item: ItemModel) -> None: ...
