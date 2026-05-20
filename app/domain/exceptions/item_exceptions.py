from app.domain.exceptions.base_exception import AppError


class ItemNotFoundError(AppError):
    status_code = 404
    detail = "Item not found"
