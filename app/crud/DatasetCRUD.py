from typing import Optional

from fastapi import HTTPException
from sqlalchemy import and_
from sqlalchemy.orm import Session

from app.db.schemas import RetrofitStrategy, RetrofitStrategyBase
from app.models.RetrofitStrategyDetails import RetrofitStrategyDetails as RetrofitStrategyDetailsModel
from app.crud.base import CRUDBase


class DatasetCRUD(CRUDBase[RetrofitStrategyDetailsModel, RetrofitStrategyBase, RetrofitStrategy]):
    def get_rsdetails(self, db: Session, dataset_id: str) -> Optional[RetrofitStrategy]:

        return (
            db.query(RetrofitStrategyDetailsModel)
            .filter(and_(RetrofitStrategyDetailsModel.dataset_id == dataset_id))
            .first()
        )

    def delete_rsdetails(self, db: Session, dataset_id: str) -> Optional[RetrofitStrategy]:
        if (
            db_rsdetails := db.query(RetrofitStrategyDetailsModel)
            .filter(and_(RetrofitStrategyDetailsModel.dataset_id == dataset_id))
            .first()
        ) is not None:
            try:
                db.delete(db_rsdetails)
                db.commit()
            except Exception as e:
                raise HTTPException(status_code=500, detail=e.args[0])
            return db_rsdetails
        raise HTTPException(status_code=404, detail=f"Retrofit strategy detail for dataset {dataset_id} not found")


datasetCRUD = DatasetCRUD(RetrofitStrategyDetailsModel)
