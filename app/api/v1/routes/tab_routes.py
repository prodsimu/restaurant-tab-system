from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.v1.schemas.tab_schema import (
    TabCreateSchema,
)
from app.application.services.tab_service import TabService
from app.infrastructure.database.database import get_db

router = APIRouter()


# GET


@router.get("/tabs/{number}")
def get_tab_by_number(number: int, db: Session = Depends(get_db)):

    try:

        tab = TabService.get_tab_by_number(db, number)

    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

    return tab


# POST


@router.post("/tabs/{number}")
def open_tab_by_number(number: int, db: Session = Depends(get_db)):
    try:

        tab = TabService.open_tab_by_number(db, number)

        return tab

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# PUT


@router.put("/tabs/{number}")
def close_tab_by_number(number: int, db: Session = Depends(get_db)):
    try:
        tab = TabService.close_tab_by_number(db, number)

        return tab

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# DELETE


@router.delete("/tabs/{number}")
def delete_tab_by_number(number: int, db: Session = Depends(get_db)):
    try:
        tab = TabService.delete_tab_by_number(db, number)

        return tab

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
