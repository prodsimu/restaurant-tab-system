from dataclasses import dataclass

from app.domain.validators.base_validator import BaseValidator


@dataclass
class TabCreateEntity:
    number: int

    def validate(self) -> None:
        self.number = BaseValidator.validate_non_empty(str(self.number), "number")
        self.number = int(self.number)
