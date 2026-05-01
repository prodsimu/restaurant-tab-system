class BaseValidator:

    @staticmethod
    def validate_non_empty(value: str, field: str) -> str:
        if not value.strip():
            raise ValueError(f"{field} cannot be empty or whitespace-only.")
        return value
