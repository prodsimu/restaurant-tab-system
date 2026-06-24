from typing import Callable

from sqlalchemy.orm import Session

from app.infrastructure.database.repositories.item_repository import ItemRepository
from app.infrastructure.database.repositories.product_repository import (
    ProductRepository,
)
from app.infrastructure.database.repositories.tab_repository import TabRepository
from app.infrastructure.database.repositories.user_repository import UserRepository


class UnitOfWork:

    def __init__(self, session_factory: Callable[[], Session]):
        self.session_factory = session_factory

    def __enter__(self) -> "UnitOfWork":
        self.db: Session = self.session_factory()

        self.tabs = TabRepository(self.db)
        self.products = ProductRepository(self.db)
        self.items = ItemRepository(self.db)
        self.users = UserRepository(self.db)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type is not None:
            self.db.rollback()
        else:
            self.db.commit()

        self.db.close()
