import json

from fastapi import APIRouter, Depends, HTTPException
from typing import Any

from app import crud
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db import schemas
from app.models import RetrofitStrategyDetails

router = APIRouter()


@router.get("/{dataset_id}/rsdetails", response_model=schemas.RetrofitStrategy)
def get_retrofit_strategy_details(dataset_id: str, db:Session = Depends(get_db)) -> Any:
    rs_details = crud.datasetCRUD.get_rsdetails(db, dataset_id=dataset_id)
    if rs_details is None:
        raise HTTPException(status_code=404, detail="retrofit strategy details not found")
    return rs_details


@router.post("/{dataset_id}/rsdetails", response_model=schemas.RetrofitStrategy)
def post_retrofit_strategy_details(
    dataset_id:str,
    rsdetails: dict,
    db: Session = Depends(get_db),
) -> Any:
    # Check if an entry with this dataset_id already exists
    existing_entry = crud.datasetCRUD.get_rsdetails(db, dataset_id=dataset_id)
    if existing_entry:
        raise HTTPException(status_code=400, detail=f"Entry with dataset_id={dataset_id} already exists.")

    rsdetails["dataset_id"] = dataset_id
    try:
        rs_details = crud.datasetCRUD.create(db, obj_in=rsdetails)
    except Exception as e:
        # Log the exception or handle it as necessary
        raise HTTPException(status_code=500, detail="An error occurred while inserting the data.")

    return rs_details

@router.delete("/{dataset_id}/rsdetails", response_model=schemas.RetrofitStrategy)
def delete_retrofit_strategy_details(dataset_id: str, db: Session = Depends(get_db)) -> Any:
    return crud.datasetCRUD.delete_rsdetails(db, dataset_id)
