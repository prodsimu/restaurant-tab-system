from datetime import datetime


class BaseValidator:

    @staticmethod
    def validate_non_empty(value: str, field: str) -> str:
        if not value.strip():
            raise ValueError(f"{field} cannot be empty or whitespace-only.")
        return value

    @staticmethod
    def validate_positive_int(value: int, field: str) -> int:
        if value <= 0:
            raise ValueError(f"{field} must be greater than 0.")
        return value

    @staticmethod
    def validate_boolean(value: bool, field: str) -> bool:
        if not isinstance(value, bool):
            raise ValueError(f"{field} must be a boolean value.")
        return value

    @staticmethod
    def validate_datetime(value, field: str):
        if not isinstance(value, datetime):
            raise ValueError(f"{field} must be a datetime string.")
        return value

    @staticmethod
    def validate_none(value, field: str):
        if value is not None:
            raise ValueError(f"{field} must be None.")
        return value
