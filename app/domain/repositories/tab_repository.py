from abc import ABC, abstractmethod

from app.infrastructure.database.models.tab_model import TabModel


class TabRepositoryInterface(ABC):

    @abstractmethod
    def get_open_tab_by_number(self, tab_number: int) -> TabModel: ...
