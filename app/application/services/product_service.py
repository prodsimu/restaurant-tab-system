from app.api.v1.schemas.product_schema import ProductCreateSchema, ProductUpdateSchema
from app.domain.entities.product_entity import ProductCreateEntity, ProductUpdateEntity
from app.domain.exceptions.product_exceptions import ProductNotFoundError
from app.infrastructure.database.models.product_model import ProductModel
from app.infrastructure.database.unit_of_work import UnitOfWork


class ProductService:

    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    # CREATE

    def create_product(self, data: ProductCreateSchema) -> ProductModel:
        with self.uow as uow:
            entity = ProductCreateEntity(**data.dict())
            return uow.products.create_product(name=entity.name, price=entity.price)

    # READ

    def list_all_products(self) -> list[ProductModel]:
        with self.uow as uow:
            return uow.products.list_all_products()

    def get_product_by_id(self, product_id: int) -> ProductModel:
        with self.uow as uow:
            product = uow.products.get_product_by_id(product_id)

            if not product:
                raise ProductNotFoundError(f"Product with id {product_id} not found")

            return product

    # UPDATE

    def update_product(
        self, product_id: int, data: ProductUpdateSchema
    ) -> ProductModel:
        with self.uow as uow:
            entity = ProductUpdateEntity(**data.dict())

            update_data = {
                k: v
                for k, v in {
                    "name": entity.name,
                    "price": entity.price,
                }.items()
                if v is not None
            }

            updated_product = uow.products.update_product(product_id, update_data)

            if not updated_product:
                raise ProductNotFoundError(f"Product with id {product_id} not found")

            return updated_product

    # DELETE

    def delete_product(self, product_id: int) -> dict:
        with self.uow as uow:
            deleted_product = uow.products.delete_product(product_id)

            if not deleted_product:
                raise ProductNotFoundError(f"Product with id {product_id} not found")

        return {"message": f"Product with id {product_id} deleted successfully."}
