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
