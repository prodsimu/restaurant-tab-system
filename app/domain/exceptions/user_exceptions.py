from app.domain.exceptions.base_exception import AppError


class UserNotFoundError(AppError):
    def __init__(self, detail: str = "User not found"):
        super().__init__(status_code=404, detail=detail)


class UserAlreadyExistsError(AppError):
    def __init__(self, detail: str = "User already exists"):
        super().__init__(status_code=409, detail=detail)


class InvalidCredentialsError(AppError):
    def __init__(self, detail: str = "Invalid credentials"):
        super().__init__(status_code=401, detail=detail)


class UnauthorizedError(AppError):
    def __init__(self, detail: str = "Unauthorized"):
        super().__init__(status_code=401, detail=detail)


class ForbiddenError(AppError):
    def __init__(self, detail: str = "Forbidden"):
        super().__init__(status_code=403, detail=detail)
