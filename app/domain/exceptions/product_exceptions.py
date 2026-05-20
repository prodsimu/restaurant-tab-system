from app.domain.exceptions.base_exception import AppError


class ProductNotFoundError(AppError):
    status_code = 404
    detail = "Product not found"
