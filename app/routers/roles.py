from fastapi import APIRouter, Depends

from app import crud
from app.db import schemas
from sqlalchemy.orm import Session
from app.models.Role import RoleEnum
from app.db.database import get_db

router = APIRouter()


@router.get("", response_model=list[schemas.Role])
def read_roles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    roles = crud.roleCRUD.get_multi(db, skip=skip, limit=limit)
    return roles


@router.post("", response_model=schemas.Role)
def create_roles(name: RoleEnum, description: str, db: Session = Depends(get_db)):
    role = {
        "name": name.value,
        "description": description
    }
    new_role = crud.roleCRUD.create(db, obj_in=role)
    return new_role
