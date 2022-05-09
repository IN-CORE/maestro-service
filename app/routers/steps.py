from fastapi import APIRouter, HTTPException, Depends

from app.crud import StepCRUD
from app.db import schemas

from sqlalchemy.orm import Session

from app.db.database import get_db

router = APIRouter()


@router.get("", response_model=list[schemas.Step])
def read_steps(db: Session = Depends(get_db)):
    steps = StepCRUD.get_steps(db)
    return steps


@router.get("/{step_id}/{substep_id}", response_model=schemas.Step)
def read_step(step_id: str, substep_id: str, db: Session = Depends(get_db)):
    db_step = StepCRUD.get_step(db, step_id, substep_id)
    if db_step is None:
        raise HTTPException(status_code=404, detail="Step/SubStep not found")
    return db_step


@router.post("", response_model=schemas.Step)
def create_step(step: schemas.StepCreated, db: Session = Depends(get_db)
):
    return StepCRUD.create_step(db, step)


@router.patch("/{step_id}/{substep_id}", response_model=schemas.Step)
def update_step_status(step_id: str, substep_id: str, status: str, db: Session = Depends(get_db)):
    return StepCRUD.update_step(db, step_id, substep_id, status)


@router.delete("/{step_id}/{substep_id}", response_model=schemas.Step)
def delete_step(step_id: str, substep_id: str, db: Session = Depends(get_db)):
    return StepCRUD.delete_step(db, step_id, substep_id)