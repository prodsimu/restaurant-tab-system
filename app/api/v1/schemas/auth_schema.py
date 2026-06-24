from pydantic import BaseModel


class LoginSchema(BaseModel):
    username: str
    password: str


class TokenSchema(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserCreateSchema(BaseModel):
    username: str
    password: str
    role: str = "waiter"


class UserResponseSchema(BaseModel):
    id: int
    username: str
    role: str

    model_config = {"from_attributes": True}
