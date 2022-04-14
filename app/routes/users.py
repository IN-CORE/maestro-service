from fastapi import APIRouter, HTTPException, Depends

from app.crud import crud
from app.db import schemas

from sqlalchemy.orm import Session

from app.main import get_db

router = APIRouter()


@router.get("", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/{user_id}/roles/", response_model=schemas.Role)
def create_role_for_user(
        user_id: int, role: schemas.RoleCreate, db: Session = Depends(get_db)
):
    return crud.create_user_role(db=db, role=role, user_id=user_id)