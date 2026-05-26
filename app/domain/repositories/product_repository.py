from abc import ABC, abstractmethod

from app.infrastructure.database.models.product_model import ProductModel


class ProductRepositoryInterface(ABC):

    # CREATE

    @abstractmethod
    def create_product(self, name: str, price: float) -> ProductModel: ...

    # READ

    @abstractmethod
    def list_all_products(self) -> list[ProductModel]: ...

    @abstractmethod
    def get_product_by_id(self, product_id: int) -> ProductModel: ...

    # UPDATE

    @abstractmethod
    def update_product(
        self, product_id: int, name: str, price: float
    ) -> ProductModel: ...

    # DELETE
