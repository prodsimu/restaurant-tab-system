from fastapi import APIRouter, Depends

from app.api.v1.dependencies import get_unit_of_work, require_admin, require_waiter
from app.api.v1.schemas.product_schema import (
    ProductCreateSchema,
    ProductResponseSchema,
    ProductUpdateSchema,
)
from app.application.services.product_service import ProductService
from app.infrastructure.database.models.user_model import UserModel
from app.infrastructure.database.unit_of_work import UnitOfWork

router = APIRouter(tags=["Products"])


def get_product_service(uow: UnitOfWork = Depends(get_unit_of_work)) -> ProductService:
    return ProductService(uow)


# GET


@router.get("/products", response_model=list[ProductResponseSchema])
def list_all_products(
    service: ProductService = Depends(get_product_service),
    _: UserModel = Depends(require_waiter),
) -> list[ProductResponseSchema]:
    return service.list_all_products()


@router.get("/products/{product_id}", response_model=ProductResponseSchema)
def get_product_by_id(
    product_id: int,
    service: ProductService = Depends(get_product_service),
    _: UserModel = Depends(require_waiter),
) -> ProductResponseSchema:
    return service.get_product_by_id(product_id)


# POST


@router.post("/products", response_model=ProductResponseSchema)
def create_product(
    data: ProductCreateSchema,
    service: ProductService = Depends(get_product_service),
    _: UserModel = Depends(require_admin),
) -> ProductResponseSchema:
    return service.create_product(data)


# PATCH


@router.patch("/products/{product_id}", response_model=ProductResponseSchema)
def update_product(
    product_id: int,
    data: ProductUpdateSchema,
    service: ProductService = Depends(get_product_service),
    _: UserModel = Depends(require_admin),
) -> ProductResponseSchema:
    return service.update_product(product_id, data)


# DELETE


@router.delete("/products/{product_id}")
def delete_product(
    product_id: int,
    service: ProductService = Depends(get_product_service),
    _: UserModel = Depends(require_admin),
) -> dict:
    return service.delete_product(product_id)
