from sqlalchemy import Column, Integer

from app.infrastructure.database.database import Base


class ItemModel(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    tab_number = Column(Integer, index=True)
    product_id = Column(Integer, index=True)
    quantity = Column(Integer)
