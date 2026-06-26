from dataclasses import dataclass, field
from datetime import datetime, timezone

from app.domain.validators.base_validator import BaseValidator


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


@dataclass
class TabCreateEntity:
    number: int
    is_open: bool = True
    created_at: datetime = field(default_factory=utc_now)
    closed_at: None = None

    def __post_init__(self):
        self.validate()

    def validate(self) -> None:
        self.number = BaseValidator.validate_positive_int(self.number, "number")
        self.is_open = BaseValidator.validate_boolean(self.is_open, "is_open")
        self.created_at = BaseValidator.validate_datetime(self.created_at, "created_at")
        self.closed_at = BaseValidator.validate_none(self.closed_at, "closed_at")
