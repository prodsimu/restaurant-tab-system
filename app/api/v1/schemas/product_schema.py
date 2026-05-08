from pydantic import BaseModel, Field


class ProductBaseSchema(BaseModel):
    name: str = Field(max_length=100, nullable=False)
    price: float = Field(gt=0)


class ProductCreateSchema(ProductBaseSchema):
    pass


class ProductUpdateSchema(ProductBaseSchema):
    name: str | None = Field(max_length=100, default=None)
    price: float | None = Field(gt=0, default=None)


class ProductResponseSchema(BaseModel):
    id: int
    name: str
    price: float

    model_config = {"from_attributes": True}
