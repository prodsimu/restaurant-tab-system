from fastapi import APIRouter, Depends

from app.api.v1.dependencies import get_unit_of_work, require_admin
from app.api.v1.schemas.auth_schema import (
    LoginSchema,
    TokenSchema,
    UserCreateSchema,
    UserResponseSchema,
)
from app.application.services.auth_service import AuthService
from app.infrastructure.database.models.user_model import UserModel
from app.infrastructure.database.unit_of_work import UnitOfWork

router = APIRouter(prefix="/auth", tags=["Auth"])


def get_auth_service(uow: UnitOfWork = Depends(get_unit_of_work)) -> AuthService:
    return AuthService(uow)


@router.post("/login", response_model=TokenSchema)
def login(data: LoginSchema, service: AuthService = Depends(get_auth_service)):
    return service.login(data)


@router.post("/register", response_model=UserResponseSchema)
def register(
    data: UserCreateSchema,
    service: AuthService = Depends(get_auth_service),
    _: UserModel = Depends(require_admin),
):
    return service.register(data)
