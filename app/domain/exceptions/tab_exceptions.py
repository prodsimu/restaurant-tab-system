from app.domain.exceptions.base_exception import AppError


class TabNotFoundError(AppError):
    status_code = 404
    detail = "Tab not found"


class TabAlreadyExistsError(AppError):
    status_code = 409
    detail = "Tab already exists"


class TabAlreadyOpenError(AppError):
    status_code = 400
    detail = "Tab is already open"


class TabAlreadyClosedError(AppError):
    status_code = 400
    detail = "Tab is already closed"
