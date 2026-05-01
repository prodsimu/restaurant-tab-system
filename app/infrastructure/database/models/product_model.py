from sqlalchemy import Column, Integer, String

from app.infrastructure.database.database import Base


class ProductModel(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    barcode = Column(String, unique=True, index=True)
    price = Column(Integer)
