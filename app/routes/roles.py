from fastapi import APIRouter, Depends

from app.crud import crud
from app.db import schemas
from sqlalchemy.orm import Session

from app.main import get_db

router = APIRouter()


@router.get("", response_model=list[schemas.Role])
def read_roles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    roles = crud.get_roles(db, skip=skip, limit=limit)
    return roles
