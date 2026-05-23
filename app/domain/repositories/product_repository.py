from abc import ABC, abstractmethod

from app.infrastructure.database.models.product_model import ProductModel


class ProductRepositoryInterface(ABC):

    @abstractmethod
    def create_product(self, name: str, price: float) -> ProductModel: ...
