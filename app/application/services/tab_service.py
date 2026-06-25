from dataclasses import dataclass
from datetime import datetime, timezone

from app.domain.entities.tab_entity import TabCreateEntity
from app.domain.exceptions.tab_exceptions import (
    TabAlreadyClosedError,
    TabAlreadyOpenError,
    TabNotFoundError,
)
from app.infrastructure.database.models.tab_model import TabModel
from app.infrastructure.database.unit_of_work import UnitOfWork


@dataclass
class TabWithTotal:
    id: int
    number: int
    is_open: bool
    created_at: datetime
    closed_at: datetime | None
    waiter_id: int
    total: float | None = None


class TabService:

    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    # CREATE

    def open_tab_by_number(self, number: int, waiter_id: int) -> TabModel:
        with self.uow as uow:
            open_tab = uow.tabs.get_open_tab_by_number(number)

            if open_tab:
                raise TabAlreadyOpenError(
                    f"An open tab with number {number} already exists."
                )

            entity = TabCreateEntity(number, True, datetime.now(timezone.utc), None)

            return uow.tabs.open_tab_by_number(
                number=entity.number,
                is_open=entity.is_open,
                created_at=entity.created_at,
                closed_at=entity.closed_at,
                waiter_id=waiter_id,
            )

    # READ

    def list_all_tabs(self) -> list[TabModel]:
        with self.uow as uow:
            tabs = uow.tabs.list_all_tabs()

            if not tabs:
                raise TabNotFoundError("No tabs found.")

            return tabs

    def list_tabs_by_number(self, number: int) -> list[TabModel]:
        with self.uow as uow:
            tabs = uow.tabs.list_tabs_by_number(number)

            if not tabs:
                raise TabNotFoundError(f"Tabs with number {number} not found.")

            return tabs

    def get_tab_total(self, number: int) -> TabWithTotal:
        with self.uow as uow:
            tab = uow.tabs.get_open_tab_by_number(number)

            if not tab:
                raise TabNotFoundError(f"No open tab with number {number} found.")

            return self._calculate_total(uow, tab)

    # UPDATE

    def close_tab_by_number(self, number: int) -> TabWithTotal:
        with self.uow as uow:
            tab = uow.tabs.get_open_tab_by_number(number)

            if not tab:
                raise TabAlreadyClosedError(f"No open tab with number {number} exists.")

            tab_with_total = self._calculate_total(uow, tab)

            closed_tab = uow.tabs.close_tab_by_number(
                number, datetime.now(timezone.utc)
            )

            tab_with_total.is_open = closed_tab.is_open
            tab_with_total.closed_at = closed_tab.closed_at

            return tab_with_total

    # DELETE

    def delete_tab_by_id(self, id: int) -> dict:
        with self.uow as uow:
            deleted_tab = uow.tabs.delete_tab_by_id(id)

            if not deleted_tab:
                raise TabNotFoundError(f"Tab with ID {id} not found.")

        return {"message": f"Tab with ID {id} deleted successfully"}

    # PRIVATE

    def _calculate_total(self, uow, tab: TabModel) -> TabWithTotal:
        items = uow.items.list_items_by_tab(tab.id)

        total = 0.0
        for item in items:
            product = uow.products.get_product_by_id(item.product_id)
            if product:
                total += item.quantity * product.price

        return TabWithTotal(
            id=tab.id,
            number=tab.number,
            is_open=tab.is_open,
            created_at=tab.created_at,
            closed_at=tab.closed_at,
            waiter_id=tab.waiter_id,
            total=round(total, 2),
        )
