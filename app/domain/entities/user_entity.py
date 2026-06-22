from dataclasses import dataclass

from app.domain.validators.base_validator import BaseValidator


@dataclass
class UserCreateEntity:
    username: str
    password_hash: str
    role: str

    def __post_init__(self):
        self.validate()

    def validate(self):
        self.username = BaseValidator.validate_string(self.username, "username")
        self.password_hash = BaseValidator.validate_string(
            self.password_hash, "password_hash"
        )
        self.role = BaseValidator.validate_string(self.role, "role")
