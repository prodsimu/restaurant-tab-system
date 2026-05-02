from app.api.v1.schemas.tab_schema import TabCreateSchema
from app.application.services.tab_service import TabService
from tests.test_database import Base, SessionLocal, engine


def test_create_tab():

    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    data = TabCreateSchema(number=1)

    tab = TabService.create_tab(db, data)

    assert tab.number == data.number
    assert tab.is_empty
