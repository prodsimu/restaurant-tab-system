from sqlalchemy import Boolean, Column, Integer

from app.infrastructure.database.database import Base


class TabModel(Base):
    __tablename__ = "tabs"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, unique=True)
    is_empty = Column(Boolean, default=True)
