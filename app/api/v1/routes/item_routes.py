from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.v1.schemas.item_schema import ItemCreateSchema, ItemResponseSchema
from app.application.services.item_service import ItemService
from app.infrastructure.database.database import get_db

router = APIRouter(tags=["Items"])

# GET

# POST


@router.post("/items", response_model=ItemResponseSchema)
def add_item_to_tab(data: ItemCreateSchema, db: Session = Depends(get_db)):
    try:

        return ItemService.add_item_to_tab(db, data)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# PUT

# DELETE
