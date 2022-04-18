from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.db import schemas
from app.models import Step


def get_step(db: Session, step_id: str, substep_id: str):
    return db.query(Step).filter(Step.step_id == step_id and Step.substep_id == substep_id).first()


def get_steps(db: Session):
    return db.query(Step).all()


def create_step(db: Session, step: schemas.StepCreated):
    try:
        db_step = Step(**step.dict())
        db.add(db_step)
        db.commit()
        db.refresh(db_step)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.args[0])
    return db_step


def update_step(db:Session, step_id: str, substep_id: str, step: schemas.StepUpdated):
    if (
        db_step := db.query(Step).filter(Step.step_id == step_id and Step.substep_id == substep_id).first()
    ) is not None:
        try:
            db_step.update(step)
            db.commit()
            db.refresh(db_step)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e.args[0])
        return db_step
    raise HTTPException(status_code=404, detail=f"Step {step_id}/{substep_id} not found")
