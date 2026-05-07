from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.v1.schemas.product_schema import ProductCreateSchema
from app.application.services.product_service import ProductService
from app.infrastructure.database.database import get_db

router = APIRouter()


# GET

# POST


@router.post("/products")
def create_product(data: ProductCreateSchema, db: Session = Depends(get_db)):
    try:
        product = ProductService.create_product(db, data)

        return product

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# PUT

# DELETE
