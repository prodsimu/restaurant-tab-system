from pydantic import BaseModel, Field


class ProductBaseSchema(BaseModel):
    name: str = Field(max_length=100)
    barcode: str = Field(max_length=50)
    price: float = Field(gt=0)


class ProductCreateSchema(ProductBaseSchema):
    pass
