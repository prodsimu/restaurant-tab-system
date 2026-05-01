from pydantic import BaseModel, Field


class TabBaseSchema(BaseModel):
    number: int = Field(gt=0)


class TabCreateSchema(TabBaseSchema):
    pass
