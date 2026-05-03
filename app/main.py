from fastapi import FastAPI

from app.api.v1.routes.tab_routes import router as tab_router
from app.infrastructure.database.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(tab_router)
