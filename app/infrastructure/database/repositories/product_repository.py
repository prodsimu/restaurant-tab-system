from sqlalchemy.orm import Session

from app.domain.repositories.product_repository import ProductRepositoryInterface
from app.infrastructure.database.models.product_model import ProductModel


class ProductRepository(ProductRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db
