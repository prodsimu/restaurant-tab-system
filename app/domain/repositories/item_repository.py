from abc import ABC, abstractmethod

from app.infrastructure.database.models.item_model import ItemModel


class ItemRepositoryInterface(ABC):

    @abstractmethod
    def create_item(self, tab_id: int, product_id: int, quantity: int) -> ItemModel: ...

    @abstractmethod
    def get_item_by_id(self, item_id: int) -> ItemModel: ...
