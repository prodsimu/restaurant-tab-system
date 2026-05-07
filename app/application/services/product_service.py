from sqlalchemy.orm import Session

from app.api.v1.schemas.product_schema import ProductCreateSchema
from app.domain.entities.product_entity import ProductCreateEntity
from app.domain.exceptions.product_exceptions import ProductNotFoundError
from app.infrastructure.database.models.product_model import ProductModel


class ProductService:

    # CREATE

    @staticmethod
    def create_product(db: Session, data: ProductCreateSchema):
        from app.infrastructure.database.models.product_model import ProductModel

        entity = ProductCreateEntity(**data.dict())
        entity.validate()
        entity.normalize()

        db_model = ProductModel(name=entity.name, price=entity.price)

        db.add(db_model)
        db.commit()
        db.refresh(db_model)

        return db_model

    # READ

    @staticmethod
    def get_product_by_id(db: Session, product_id: int):
        product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

        if not product:
            raise ProductNotFoundError(f"Product with id {product_id} not found")

        return product
