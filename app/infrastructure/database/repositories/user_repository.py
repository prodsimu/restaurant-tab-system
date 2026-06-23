from sqlalchemy.orm import Session

from app.domain.repositories.user_repository import UserRepositoryInterface
from app.infrastructure.database.models.user_model import UserModel


class UserRepository(UserRepositoryInterface):

    def __init__(self, db: Session):
        self.db = db

    # CREATE

    def create_user(self, username: str, password_hash: str, role: str) -> UserModel:
        user = UserModel(username=username, password_hash=password_hash, role=role)
        self.db.add(user)
        self.db.flush()
        self.db.refresh(user)
        return user

    # READ

    def get_user_by_id(self, user_id: int) -> UserModel | None:
        return self.db.query(UserModel).filter(UserModel.id == user_id).first()

    def get_user_by_username(self, username: str) -> UserModel | None:
        return self.db.query(UserModel).filter(UserModel.username == username).first()
