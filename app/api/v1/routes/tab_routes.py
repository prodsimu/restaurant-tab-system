from fastapi import APIRouter, Depends

from app.api.v1.schemas.tab_schema import TabResponseSchema
from app.application.services.tab_service import TabService
from app.infrastructure.database.database import SessionLocal
from app.infrastructure.database.unit_of_work import UnitOfWork

router = APIRouter(tags=["Tabs"])


def get_unit_of_work() -> UnitOfWork:
    return UnitOfWork(session_factory=SessionLocal)


def get_tab_service(uow: UnitOfWork = Depends(get_unit_of_work)) -> TabService:
    return TabService(uow)


# GET


@router.get("/tabs", response_model=list[TabResponseSchema])
def list_all_tabs(
    service: TabService = Depends(get_tab_service),
) -> list[TabResponseSchema]:
    return service.list_all_tabs()


@router.get("/tabs/{number}/total", response_model=TabResponseSchema)
def get_tab_total(
    number: int, service: TabService = Depends(get_tab_service)
) -> TabResponseSchema:
    return service.get_tab_total(number)


@router.get("/tabs/{number}", response_model=list[TabResponseSchema])
def list_tabs_by_number(
    number: int, service: TabService = Depends(get_tab_service)
) -> list[TabResponseSchema]:
    return service.list_tabs_by_number(number)


# POST


@router.post("/tabs/{number}", response_model=TabResponseSchema)
def open_tab_by_number(
    number: int, service: TabService = Depends(get_tab_service)
) -> TabResponseSchema:
    return service.open_tab_by_number(number)


# PUT


@router.put("/tabs/{number}", response_model=TabResponseSchema)
def close_tab_by_number(
    number: int, service: TabService = Depends(get_tab_service)
) -> TabResponseSchema:
    return service.close_tab_by_number(number)


# DELETE


@router.delete("/tabs/{id}")
def delete_tab_by_id(id: int, service: TabService = Depends(get_tab_service)) -> dict:
    return service.delete_tab_by_id(id)
