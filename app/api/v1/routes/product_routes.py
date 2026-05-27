from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.v1.schemas.product_schema import (
    ProductCreateSchema,
    ProductResponseSchema,
    ProductUpdateSchema,
)
from app.application.services.product_service import ProductService
from app.infrastructure.database.database import get_db
from app.infrastructure.database.repositories.product_repository import (
    ProductRepository,
)

router = APIRouter(tags=["Products"])


def get_product_service(db: Session = Depends(get_db)) -> ProductService:
    return ProductService(ProductRepository(db))


# GET


@router.get("/products", response_model=list[ProductResponseSchema])
def list_all_products(
    service: ProductService = Depends(get_product_service),
) -> list[ProductResponseSchema]:
    return service.list_all_products()


@router.get("/products/{product_id}", response_model=ProductResponseSchema)
def get_product_by_id(
    product_id: int, service: ProductService = Depends(get_product_service)
) -> ProductResponseSchema:
    return service.get_product_by_id(product_id)


# POST


@router.post("/products", response_model=ProductResponseSchema)
def create_product(
    data: ProductCreateSchema, service: ProductService = Depends(get_product_service)
) -> ProductResponseSchema:
    return service.create_product(data)


# PATCH


@router.patch("/products/{product_id}", response_model=ProductResponseSchema)
def update_product(
    product_id: int,
    data: ProductUpdateSchema,
    service: ProductService = Depends(get_product_service),
) -> ProductResponseSchema:
    return service.update_product(product_id, data)


# DELETE


@router.delete("/products/{product_id}")
def delete_product(
    product_id: int, service: ProductService = Depends(get_product_service)
) -> dict:
    return service.delete_product(product_id)
