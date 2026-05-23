from abc import ABC, abstractmethod

from app.infrastructure.database.models.product_model import ProductModel


class ProductRepositoryInterface(ABC):

    # CREATE

    @abstractmethod
    def create_product(self, name: str, price: float) -> ProductModel: ...

    # READ

    @abstractmethod
    def list_all_products(self) -> list[ProductModel]: ...

    # UPDATE

    # DELETE
