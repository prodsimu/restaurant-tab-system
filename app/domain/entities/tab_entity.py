from dataclasses import dataclass

from app.domain.validators.base_validator import BaseValidator


@dataclass
class TabCreateEntity:
    number: int
    is_empty: bool = True

    def validate(self) -> None:
        self.number = BaseValidator.validate_positive_int(self.number, "number")
        self.is_empty = BaseValidator.validate_boolean(self.is_empty, "is_empty")
