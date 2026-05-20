from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.v1.schemas.item_schema import ItemCreateSchema, ItemResponseSchema
from app.application.services.item_service import ItemService
from app.infrastructure.database.database import get_db

router = APIRouter(tags=["Items"])

# GET


@router.get("/items/{tab_number}", response_model=list[ItemResponseSchema])
def list_tab_items(
    tab_number: int, db: Session = Depends(get_db)
) -> list[ItemResponseSchema]:
    return ItemService.list_tab_items(db, tab_number)


# POST


@router.post("/items", response_model=ItemResponseSchema)
def add_item_to_tab(
    data: ItemCreateSchema, db: Session = Depends(get_db)
) -> ItemResponseSchema:
    return ItemService.add_item_to_tab(db, data)


# DELETE


@router.delete("/items/{item_id}")
def delete_item_from_tab(item_id: int, db: Session = Depends(get_db)) -> dict[str, str]:
    return ItemService.delete_item_from_tab(db, item_id)
