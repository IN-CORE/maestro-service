from typing import Any
from fastapi import APIRouter, HTTPException, Depends

from app import crud
from app.db import schemas

from sqlalchemy.orm import Session

from app.db.database import get_db

router = APIRouter()


@router.get("", response_model=list[schemas.User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> Any:
    users = crud.userCRUD.get_multi(db, skip=skip, limit=limit)
    return users


@router.post("", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)) -> Any:
    db_user = crud.userCRUD.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.userCRUD.create(db, obj_in=user)


@router.get("/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)) -> Any:
    db_user = crud.userCRUD.get(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.delete("/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)) -> Any:
    db_user = crud.userCRUD.remove(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found and cannot be deleted")
    return db_user


@router.post("/{user_id}/roles/{role_id}", response_model=schemas.User)
def attach_role_to_user(
        user_id: int, role_id: int, db: Session = Depends(get_db)
) -> Any:
    return crud.userCRUD.attach_user_role(db=db, user_id=user_id, role_id=role_id)
