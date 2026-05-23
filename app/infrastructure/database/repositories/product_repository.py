from sqlalchemy.orm import Session

from app.domain.repositories.product_repository import ProductRepositoryInterface
from app.infrastructure.database.models.product_model import ProductModel


class ProductRepository(ProductRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db

    def create_product(self, name: str, price: float) -> ProductModel:
        db_model = ProductModel(name=name, price=price)

        self.db.add(db_model)
        self.db.commit()
        self.db.refresh(db_model)

        return db_model
