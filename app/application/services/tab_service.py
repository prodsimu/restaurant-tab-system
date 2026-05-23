from datetime import datetime, timezone

from app.domain.entities.tab_entity import TabCreateEntity
from app.domain.exceptions.tab_exceptions import (
    TabAlreadyClosedError,
    TabAlreadyOpenError,
    TabNotFoundError,
)
from app.infrastructure.database.models.tab_model import TabModel
from app.infrastructure.database.repositories.tab_repository import TabRepository


class TabService:

    def __init__(self, repo: TabRepository):
        self.repo = repo

    # CREATE

    def open_tab_by_number(self, number: int) -> TabModel:

        open_tab = self.repo.get_open_tab_by_number(number)

        if open_tab:
            raise TabAlreadyOpenError(
                f"An open tab with number {number} already exists."
            )

        entity = TabCreateEntity(number, True, datetime.now(timezone.utc), None)

        tab = self.repo.open_tab_by_number(
            number=entity.number,
            is_open=entity.is_open,
            created_at=entity.created_at,
            closed_at=entity.closed_at,
        )

        return tab

    # READ

    def list_all_tabs(self) -> list[TabModel]:
        tabs = self.repo.list_all_tabs()

        if not tabs:
            raise TabNotFoundError("No tabs found.")

        return tabs

    def list_tabs_by_number(self, number: int) -> TabModel:
        tabs = self.repo.list_tabs_by_number(number)

        if not tabs:
            raise TabNotFoundError(f"Tabs with number {number} not found.")

        return tabs

    # UPDATE

    def close_tab_by_number(self, number: int) -> TabModel:

        tab = self.repo.get_open_tab_by_number(number)

        if not tab:
            raise TabAlreadyClosedError(f"No open tab with number {number} exists.")

        closed_tab = self.repo.close_tab_by_number(number, datetime.now(timezone.utc))

        return closed_tab

    # DELETE

    def delete_tab_by_id(self, id: int) -> dict:

        deleted_tab = self.repo.delete_tab_by_id(id)

        if not deleted_tab:
            raise TabNotFoundError(f"Tab with ID {id} not found.")

        return {"message": f"Tab with ID {id} deleted successfully"}
