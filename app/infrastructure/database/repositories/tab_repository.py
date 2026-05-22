from datetime import datetime

from sqlalchemy.orm import Session

from app.domain.repositories.tab_repository import TabRepositoryInterface
from app.infrastructure.database.models.tab_model import TabModel


class TabRepository(TabRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db

    # CREATE

    def open_tab_by_number(
        self, number: int, is_open: bool, created_at: datetime, closed_at: datetime
    ) -> TabModel:

        model = TabModel(
            number=number,
            is_open=is_open,
            created_at=created_at,
            closed_at=closed_at,
        )

        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)

        return model

    # READ

    def get_open_tab_by_number(self, tab_number: int) -> TabModel:
        return (
            self.db.query(TabModel)
            .filter(TabModel.number == tab_number, TabModel.is_open)
            .first()
        )

    def list_all_tabs(self) -> list[TabModel]:
        return self.db.query(TabModel).all()

    def list_tabs_by_number(self, number: int) -> list[TabModel]:
        return self.db.query(TabModel).filter(TabModel.number == number).all()

    def list_open_tabs(self) -> list[TabModel]:
        return self.db.query(TabModel).filter(TabModel.is_open).all()
