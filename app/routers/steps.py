from fastapi import APIRouter, HTTPException, Depends
from app.db import schemas
from sqlalchemy.orm import Session
from typing import Any

from app.db.database import get_db
from app import crud

router = APIRouter()


@router.get("", response_model=list[schemas.Step])
def read_steps(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> Any:
    steps = crud.stepCRUD.get_multi(db, skip, limit)
    return steps


@router.get("/{step_id}/{substep_id}", response_model=schemas.Step)
def read_step(step_id: str, substep_id: str, db: Session = Depends(get_db)) -> Any:
    db_step = crud.stepCRUD.get_step(db, id=step_id, substep_id=substep_id)
    if db_step is None:
        raise HTTPException(status_code=404, detail="Step/SubStep not found")
    return db_step


@router.post("", response_model=schemas.Step)
def create_step(step: schemas.StepCreate, db: Session = Depends(get_db)) -> Any:

    new_step = crud.stepCRUD.create(db, obj_in=step)
    return new_step


@router.patch("/{step_id}/{substep_id}", response_model=schemas.Step)
def update_step_status(step_id: str, substep_id: str, status: str, db: Session = Depends(get_db)):
    return crud.stepCRUD.update_step(db, id=step_id, substep_id=substep_id, status=status)


@router.delete("/{step_id}/{substep_id}", response_model=schemas.Step)
def delete_step(step_id: str, substep_id: str, db: Session = Depends(get_db)):
    return crud.stepCRUD.delete_step(db, step_id, substep_id)
