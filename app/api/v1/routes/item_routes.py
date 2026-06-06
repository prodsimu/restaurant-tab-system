# app/api/v1/routes/item_routes.py

from fastapi import APIRouter, Depends

from app.api.v1.schemas.item_schema import ItemCreateSchema, ItemResponseSchema
from app.application.services.item_service import ItemService
from app.infrastructure.database.database import SessionLocal
from app.infrastructure.database.unit_of_work import UnitOfWork

router = APIRouter(tags=["Items"])


def get_unit_of_work() -> UnitOfWork:
    return UnitOfWork(session_factory=SessionLocal)


def get_item_service(uow: UnitOfWork = Depends(get_unit_of_work)) -> ItemService:
    return ItemService(uow)


# GET


@router.get("/items/{tab_number}", response_model=list[ItemResponseSchema])
def list_tab_items(
    tab_number: int,
    service: ItemService = Depends(get_item_service),
) -> list[ItemResponseSchema]:
    return service.list_tab_items(tab_number)


# POST


@router.post("/items", response_model=ItemResponseSchema)
def add_item_to_tab(
    data: ItemCreateSchema,
    service: ItemService = Depends(get_item_service),
) -> ItemResponseSchema:
    return service.add_item_to_tab(data)


# DELETE


@router.delete("/items/{item_id}")
def delete_item_from_tab(
    item_id: int,
    service: ItemService = Depends(get_item_service),
) -> dict[str, str]:
    return service.delete_item_from_tab(item_id)
