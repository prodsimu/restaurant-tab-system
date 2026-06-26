from datetime import datetime, timezone

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer

from app.infrastructure.database.database import Base


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class TabModel(Base):
    __tablename__ = "tabs"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, unique=False, index=True, nullable=False)
    is_open = Column(Boolean, default=True)
    created_at = Column(DateTime, default=utc_now)
    closed_at = Column(DateTime, nullable=True)
    waiter_id = Column(Integer, ForeignKey("users.id"), nullable=False)
