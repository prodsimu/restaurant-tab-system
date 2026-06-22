import enum

from sqlalchemy import Column, Enum, Integer, String

from app.infrastructure.database.database import Base


class RoleEnum(str, enum.Enum):
    admin = "admin"
    waiter = "waiter"


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(Enum(RoleEnum), nullable=False, default=RoleEnum.waiter)
