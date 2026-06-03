from abc import ABC, abstractmethod

from app.infrastructure.database.models.item_model import ItemModel


class ItemRepositoryInterface(ABC):

    # CREATE

    @abstractmethod
    def create_item(self, tab_id: int, product_id: int, quantity: int) -> ItemModel: ...

    # READ

    @abstractmethod
    def get_item_by_id(self, item_id: int) -> ItemModel: ...

    @abstractmethod
    def list_items_by_tab_id(self, tab_id: int) -> list[ItemModel]: ...

    # UPDATE

    @abstractmethod
    def increment_quantity(self, item_id: int, quantity: int) -> ItemModel: ...

    @abstractmethod
    def decrement_quantity(self, item_id: int, quantity: int) -> ItemModel: ...
