from fastapi import HTTPException
from sqlalchemy import and_
from sqlalchemy.orm import Session
from datetime import datetime

from app.db.schemas import StepCreate, StepUpdate
from app.crud.base import CRUDBase
from app.models import Step


class StepCRUD(CRUDBase[Step, StepCreate, StepUpdate]):
    def get_step(self, db: Session, id: int, substep_id: str) -> Step:

        return (
            db.query(Step)
            .filter(and_(Step.step_id == id, Step.substep_id == substep_id))
            .first()
        )

    def update_step(
        self,
        db: Session,
        id: int,
        substep_id: str,
        status: str,
        status_user_id: int,
        status_updated_at: datetime,
        doc_uri: str,
        doc_user_id: int,
        doc_updated_at: datetime,
    ):
        if (
            db_step := db.query(Step)
            .filter(and_(Step.step_id == id, Step.substep_id == substep_id))
            .first()
        ) is not None:
            try:
                db_step.status = status
                db_step.status_user_id = status_user_id
                db_step.status_updated_at = status_updated_at
                db_step.doc_uri = doc_uri
                db_step.doc_user_id = doc_user_id
                db_step.doc_updated_at = doc_updated_at
                db.commit()
                db.refresh(db_step)
            except Exception as e:
                raise HTTPException(status_code=500, detail=e.args[0])
            return db_step

        raise HTTPException(status_code=404, detail=f"Step {id}/{substep_id} not found")

    def delete_step(self, db: Session, id: int, substep_id: str):
        if (
            db_step := db.query(Step)
            .filter(and_(Step.step_id == id, Step.substep_id == substep_id))
            .first()
        ) is not None:
            try:
                db.delete(db_step)
                db.commit()
            except Exception as e:
                raise HTTPException(status_code=500, detail=e.args[0])
            return db_step
        raise HTTPException(status_code=404, detail=f"Step {id}/{substep_id} not found")


stepCRUD = StepCRUD(Step)
