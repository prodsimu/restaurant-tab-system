from pydantic import BaseModel, Field


class ItemBaseSchema(BaseModel):
    tab_number: int = Field(gt=0)
    product_id: int = Field(gt=0)
    quantity: int = Field(gt=0)


class ItemCreateSchema(ItemBaseSchema):
    pass


class ItemResponseSchema(BaseModel):
    id: int
    tab_id: int
    product_id: int
    quantity: int

    model_config = {"from_attributes": True}
