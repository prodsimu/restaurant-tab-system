from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.infrastructure.database.database import Base

TEST_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_test_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
