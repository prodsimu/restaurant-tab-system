from pydantic import BaseModel, Field


class ProductBaseSchema(BaseModel):
    name: str = Field(max_length=100)
    price: float = Field(gt=0)


class ProductCreateSchema(ProductBaseSchema):
    pass
