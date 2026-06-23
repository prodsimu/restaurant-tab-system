from abc import ABC, abstractmethod

from app.infrastructure.database.models.user_model import UserModel


class UserRepositoryInterface(ABC):

    # CREATE

    @abstractmethod
    def create_user(
        self, username: str, password_hash: str, role: str
    ) -> UserModel: ...
