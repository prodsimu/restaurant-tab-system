from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.v1.schemas.product_schema import ProductCreateSchema, ProductUpdateSchema
from app.application.services.product_service import ProductService
from app.infrastructure.database.database import get_db

router = APIRouter()


# GET


@router.get("/products/{product_id}")
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    try:
        product = ProductService.get_product_by_id(db, product_id)

        return product

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# POST


@router.post("/products")
def create_product(data: ProductCreateSchema, db: Session = Depends(get_db)):
    try:
        product = ProductService.create_product(db, data)

        return product

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# PATCH


@router.patch("/products")
def update_product(data: ProductUpdateSchema, db: Session = Depends(get_db)):
    try:
        product = ProductService.update_product(db, data)

        return product

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# DELETE
