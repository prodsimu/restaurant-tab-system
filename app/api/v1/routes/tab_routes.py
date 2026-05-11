from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.v1.schemas.tab_schema import TabResponseSchema
from app.application.services.tab_service import TabService
from app.infrastructure.database.database import get_db

router = APIRouter(tags=["Tabs"])


# GET


@router.get("/tabs/{number}", response_model=list[TabResponseSchema])
def list_tabs_by_number(number: int, db: Session = Depends(get_db)):

    try:

        tabs = TabService.list_tabs_by_number(db, number)

        return tabs

    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


# POST


@router.post("/tabs/{number}", response_model=TabResponseSchema)
def open_tab_by_number(number: int, db: Session = Depends(get_db)):
    try:

        tab = TabService.open_tab_by_number(db, number)

        return tab

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# PUT


@router.put("/tabs/{number}", response_model=TabResponseSchema)
def close_tab_by_number(number: int, db: Session = Depends(get_db)):
    try:
        tab = TabService.close_tab_by_number(db, number)

        return tab

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# DELETE


@router.delete("/tabs/{id}", response_model=TabResponseSchema)
def delete_tab_by_id(id: int, db: Session = Depends(get_db)):
    try:
        tab = TabService.delete_tab_by_id(db, id)

        return tab

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
