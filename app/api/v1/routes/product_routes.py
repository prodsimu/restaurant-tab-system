from fastapi import APIRouter, Depends
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


@router.get("/products", response_model=list[ProductResponseSchema])
def list_all_products(db: Session = Depends(get_db)) -> list[ProductResponseSchema]:
    return ProductService.list_all_products(db)


@router.get("/products/{product_id}", response_model=ProductResponseSchema)
def get_product_by_id(
    product_id: int, db: Session = Depends(get_db)
) -> ProductResponseSchema:
    return ProductService.get_product_by_id(db, product_id)


# POST


@router.post("/products", response_model=ProductResponseSchema)
def create_product(
    data: ProductCreateSchema, db: Session = Depends(get_db)
) -> ProductResponseSchema:
    return ProductService.create_product(db, data)


# PATCH


@router.patch("/products/{product_id}", response_model=ProductResponseSchema)
def update_product(
    product_id: int, data: ProductUpdateSchema, db: Session = Depends(get_db)
) -> ProductResponseSchema:
    return ProductService.update_product(db, product_id, data)


# DELETE


@router.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)) -> dict:
    return ProductService.delete_product(db, product_id)
