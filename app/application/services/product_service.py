from app.api.v1.schemas.product_schema import ProductCreateSchema, ProductUpdateSchema
from app.domain.entities.product_entity import ProductCreateEntity, ProductUpdateEntity
from app.domain.exceptions.product_exceptions import ProductNotFoundError
from app.infrastructure.database.models.product_model import ProductModel
from app.infrastructure.database.repositories.product_repository import (
    ProductRepository,
)


class ProductService:

    def __init__(self, repo: ProductRepository):
        self.repo = repo

    # CREATE

    def create_product(self, data: ProductCreateSchema) -> ProductModel:

        entity = ProductCreateEntity(**data.dict())

        return self.repo.create_product(name=entity.name, price=entity.price)

    # READ

    def list_all_products(self) -> list[ProductModel]:
        return self.repo.list_all_products()

    def get_product_by_id(self, product_id: int) -> ProductModel:
        product = self.repo.get_product_by_id(product_id)

        if not product:
            raise ProductNotFoundError(f"Product with id {product_id} not found")

        return product

    # UPDATE

    def update_product(
        self, product_id: int, data: ProductUpdateSchema
    ) -> ProductModel:

        entity = ProductUpdateEntity(**data.dict())

        updated_product = self.repo.update_product(
            product_id, entity.name, entity.price
        )

        if not updated_product:
            raise ProductNotFoundError(f"Product with id {product_id} not found")

        return updated_product

    # DELETE

    @staticmethod
    def delete_product(self, product_id: int) -> dict:

        deleted_product = self.repo.delete_product(product_id)

        if not deleted_product:
            raise ProductNotFoundError(f"Product with id {product_id} not found")

        return {"message": f"Product with id {product_id} deleted successfully."}
