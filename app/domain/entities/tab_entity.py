from dataclasses import dataclass
from datetime import datetime, timezone

from app.domain.validators.base_validator import BaseValidator


@dataclass
class TabCreateEntity:
    number: int
    is_open: bool = False
    created_at: datetime = datetime.now(timezone.utc)
    closed_at: None = None

    def validate(self) -> None:
        self.number = BaseValidator.validate_positive_int(self.number, "number")
        self.is_open = BaseValidator.validate_boolean(self.is_open, "is_open")
        self.created_at = BaseValidator.validate_datetime(self.created_at, "created_at")
        self.closed_at = BaseValidator.validate_none(self.closed_at, "closed_at")
