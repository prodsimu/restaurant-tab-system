from abc import ABC, abstractmethod
from datetime import datetime

from app.infrastructure.database.models.tab_model import TabModel


class TabRepositoryInterface(ABC):

    # CREATE

    @abstractmethod
    def open_tab_by_number(
        self, number: int, is_open: bool, created_at: datetime, closed_at: datetime
    ) -> TabModel: ...

    # READ

    @abstractmethod
    def get_open_tab_by_number(self, tab_number: int) -> TabModel: ...

    @abstractmethod
    def list_all_tabs(self) -> list[TabModel]: ...

    @abstractmethod
    def list_tabs_by_number(self, number: int) -> list[TabModel]: ...

    @abstractmethod
    def list_open_tabs(self) -> list[TabModel]: ...

    # UPDATE

    @abstractmethod
    def close_tab_by_number(self, number: int, closed_at: datetime) -> TabModel: ...

    # DELETE

    @abstractmethod
    def delete_tab_by_id(self, id: int) -> bool: ...
