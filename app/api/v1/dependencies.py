from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from app.core.security import decode_access_token
from app.domain.exceptions.user_exceptions import ForbiddenError, UnauthorizedError
from app.infrastructure.database.database import SessionLocal
from app.infrastructure.database.models.user_model import RoleEnum, UserModel
from app.infrastructure.database.unit_of_work import UnitOfWork

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_unit_of_work() -> UnitOfWork:
    return UnitOfWork(session_factory=SessionLocal)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    uow: UnitOfWork = Depends(get_unit_of_work),
) -> UserModel:
    payload = decode_access_token(token)

    user_id: str = payload.get("sub")

    if not user_id:
        raise UnauthorizedError()

    with uow as u:
        user = u.users.get_user_by_id(int(user_id))

    if not user:
        raise UnauthorizedError()

    return user


def require_admin(current_user: UserModel = Depends(get_current_user)) -> UserModel:
    if current_user.role != RoleEnum.admin:
        raise ForbiddenError()
    return current_user


def require_waiter(current_user: UserModel = Depends(get_current_user)) -> UserModel:
    if current_user.role not in (RoleEnum.admin, RoleEnum.waiter):
        raise ForbiddenError()
    return current_user
