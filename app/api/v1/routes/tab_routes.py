from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.v1.schemas.tab_schema import TabBaseSchema, TabCreateSchema
from app.application.services.tab_service import TabService
from app.infrastructure.database.database import get_db

router = APIRouter()


# GET

# POST


@router.post("/tabs")
def create_tab(data: TabBaseSchema, db: Session = Depends(get_db)):
    try:

        create_data = TabCreateSchema(number=data.number)

        tab = TabService.create_tab(db, create_data)

        return {"id": tab.id, "number": tab.number, "is_empty": tab.is_empty}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# PUT

# DELETE
