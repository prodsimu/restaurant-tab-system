from sqlalchemy.orm import Session

from app.api.v1.schemas.product_schema import ProductCreateSchema
from app.domain.entities.product_entity import ProductCreateEntity


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
