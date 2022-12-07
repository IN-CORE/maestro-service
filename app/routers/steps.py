from fastapi import APIRouter, HTTPException, Depends, Header
from app.db import schemas
from sqlalchemy.orm import Session
from typing import Any, Dict, Union
import json
from datetime import datetime

from app.db.database import get_db
from app import crud
from app.models.Step import StatusEnum

router = APIRouter()


@router.get("", response_model=list[schemas.Step])
def read_steps(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> Any:
    steps = crud.stepCRUD.get_multi(db=db, skip=skip, limit=limit)
    return steps


@router.get("/{step_id}/{substep_id}", response_model=schemas.Step)
def read_step(step_id: str, substep_id: str, db: Session = Depends(get_db)) -> Any:
    db_step = crud.stepCRUD.get_step(db, id=step_id, substep_id=substep_id)
    if db_step is None:
        raise HTTPException(status_code=404, detail="Step/SubStep not found")
    return db_step


@router.post("", response_model=schemas.Step)
def create_step(step_id: str, substep_id: str, status: StatusEnum, db: Session = Depends(get_db)) -> Any:
    step = {
        "step_id": step_id,
        "substep_id": substep_id,
        "status": status.value
    }
    new_step = crud.stepCRUD.create(db, obj_in=step)
    return new_step


@router.patch("/{step_id}/{substep_id}", response_model=schemas.Step)
def update_step_status(step_id: str, substep_id: str, status: StatusEnum, x_auth_userinfo: Union[str, None] = Header(None), db: Session = Depends(get_db)):
    try:
        user_name = json.loads(x_auth_userinfo)["preferred_username"]
    except:
        raise HTTPException(status_code=400, detail="Invalid user group header!")
    db_user = crud.userCRUD.get_user_by_username(db, user_name)
    if db_user is None:
        raise HTTPException(status_code=404, detail=f"User not found with Username: {user_name}")
    return crud.stepCRUD.update_step(db, id=step_id, substep_id=substep_id, status=status.value, user_id=db_user.id, updated_at=datetime.now())


@router.delete("/{step_id}/{substep_id}", response_model=schemas.Step)
def delete_step(step_id: str, substep_id: str, db: Session = Depends(get_db)):
    return crud.stepCRUD.delete_step(db, step_id, substep_id)
