from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.v1.schemas.product_schema import (
    ProductCreateSchema,
    ProductResponseSchema,
    ProductUpdateSchema,
)
from app.application.services.product_service import ProductService
from app.infrastructure.database.database import get_db

router = APIRouter(tags=["Products"])


# GET


@router.get("/products/{product_id}", response_model=ProductResponseSchema)
def get_product_by_id(
    product_id: int, db: Session = Depends(get_db)
) -> ProductResponseSchema:
    try:
        return ProductService.get_product_by_id(db, product_id)

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# POST


@router.post("/products", response_model=ProductResponseSchema)
def create_product(
    data: ProductCreateSchema, db: Session = Depends(get_db)
) -> ProductResponseSchema:
    try:
        return ProductService.create_product(db, data)

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# PATCH


@router.patch("/products/{product_id}", response_model=ProductResponseSchema)
def update_product(
    product_id: int, data: ProductUpdateSchema, db: Session = Depends(get_db)
) -> ProductResponseSchema:
    try:
        return ProductService.update_product(db, product_id, data)

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# DELETE


@router.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)) -> dict:
    try:
        return ProductService.delete_product(db, product_id)

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
