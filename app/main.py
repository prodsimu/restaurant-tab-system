from fastapi import FastAPI

from app.api.v1.routes.item_routes import router as item_router
from app.api.v1.routes.product_routes import router as product_router
from app.api.v1.routes.tab_routes import router as tab_router
from app.core.settings import settings
from app.infrastructure.database.database import Base, engine
from app.infrastructure.database.models.item_model import ItemModel
from app.infrastructure.database.models.product_model import ProductModel
from app.infrastructure.database.models.tab_model import TabModel
from app.infrastructure.http.exception_handlers import register_exception_handlers

app = FastAPI(title=settings.app_name, debug=settings.debug)

register_exception_handlers(app)

app.include_router(product_router)
app.include_router(tab_router)
app.include_router(item_router)
