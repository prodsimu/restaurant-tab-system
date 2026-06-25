from datetime import datetime, timezone

from pydantic import BaseModel, Field


class TabBaseSchema(BaseModel):
    number: int = Field(gt=0)


class TabCreateSchema(TabBaseSchema):
    is_open: bool = Field(default=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    closed_at: datetime | None = Field(default=None)


class TabResponseSchema(BaseModel):
    id: int
    number: int
    is_open: bool
    created_at: datetime
    closed_at: datetime | None
    waiter_id: int
    total: float | None = None

    model_config = {"from_attributes": True}
