from fastapi import FastAPI

from app.api.v1.routes.product_routes import router as product_router
from app.api.v1.routes.tab_routes import router as tab_router
from app.infrastructure.database.database import Base, engine
from app.infrastructure.database.models.product_model import ProductModel
from app.infrastructure.database.models.tab_model import TabModel

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(product_router)
app.include_router(tab_router)
