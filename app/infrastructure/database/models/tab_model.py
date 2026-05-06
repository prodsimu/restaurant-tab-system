from datetime import datetime, timezone

from sqlalchemy import Boolean, Column, DateTime, Integer

from app.infrastructure.database.database import Base


class TabModel(Base):
    __tablename__ = "tabs"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, unique=False, index=True, nullable=False)
    is_open = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    closed_at = Column(DateTime, nullable=True)
