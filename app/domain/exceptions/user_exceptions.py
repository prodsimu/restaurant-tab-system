from app.domain.exceptions.base_exception import AppError


class UserNotFoundError(AppError):
    status_code = 404
    detail = "User not found"


class UserAlreadyExistsError(AppError):
    status_code = 409
    detail = "User already exists"


class InvalidCredentialsError(AppError):
    status_code = 401
    detail = "Invalid credentials"


class UnauthorizedError(AppError):
    status_code = 401
    detail = "Unauthorized"


class ForbiddenError(AppError):
    status_code = 403
    detail = "Forbidden"
