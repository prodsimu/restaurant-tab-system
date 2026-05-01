from pydantic import BaseModel, Field


class ItemBaseSchema(BaseModel):
    tab_number: int = Field(gt=0)
    product_id: int = Field(gt=0)
    quantity: int = Field(gt=0)


class ItemCreateSchema(ItemBaseSchema):
    pass
