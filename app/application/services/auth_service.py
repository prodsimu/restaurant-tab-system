from app.api.v1.schemas.auth_schema import LoginSchema, UserCreateSchema
from app.core.security import create_access_token, hash_password, verify_password
from app.domain.exceptions.user_exceptions import (
    InvalidCredentialsError,
    UserAlreadyExistsError,
)
from app.infrastructure.database.models.user_model import UserModel
from app.infrastructure.database.unit_of_work import UnitOfWork


class AuthService:

    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    def register(self, data: UserCreateSchema) -> UserModel:
        with self.uow as uow:
            existing = uow.users.get_user_by_username(data.username)

            if existing:
                raise UserAlreadyExistsError(
                    f"Username '{data.username}' is already taken"
                )

            password_hash = hash_password(data.password)

            return uow.users.create_user(
                username=data.username,
                password_hash=password_hash,
                role=data.role,
            )

    def login(self, data: LoginSchema) -> dict:
        with self.uow as uow:
            user = uow.users.get_user_by_username(data.username)

            if not user or not verify_password(data.password, user.password_hash):
                raise InvalidCredentialsError()

            token = create_access_token(data={"sub": str(user.id), "role": user.role})

            return {"access_token": token, "token_type": "bearer"}
