from sqlalchemy.orm import Session

from app.domain.repositories.product_repository import ProductRepositoryInterface
from app.infrastructure.database.models.product_model import ProductModel


class ProductRepository(ProductRepositoryInterface):

    def __init__(self, db: Session):
        self.db = db

    # CREATE

    def create_product(self, name: str, price: float) -> ProductModel:
        db_model = ProductModel(name=name, price=price)

        self.db.add(db_model)
        self.db.commit()
        self.db.refresh(db_model)

        return db_model

    # READ

    def list_all_products(self) -> list[ProductModel]:
        return self.db.query(ProductModel).all()

    def get_product_by_id(self, product_id: int) -> ProductModel:
        return self.db.query(ProductModel).filter(ProductModel.id == product_id).first()

    # UPDATE

    def update_product(self, product_id: int, name: str, price: float) -> ProductModel:

        product = self.get_product_by_id(product_id)

        if not product:
            return None

        product.name = name
        product.price = price

        self.db.commit()
        self.db.refresh(product)

        return product

    # DELETE

    def delete_product(self, product_id: int) -> dict:
        product = self.get_product_by_id(product_id)

        if not product:
            return False

        self.db.delete(product)
        self.db.commit()

        return True
