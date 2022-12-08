import json

from fastapi import APIRouter, Depends, Request, HTTPException

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
def create_roles(request:Request, name: RoleEnum, description: str, db: Session = Depends(get_db)):
    # TODO wrap it as the dependency in the future
    user_groups = request.headers.get('x-auth-usergroup')
    if user_groups is not None:
        try:
            groups = json.loads(user_groups)
        except:
            raise HTTPException(status_code=400, detail="Invalid user group header!")

        if "incore_ncsa" in groups["groups"]:
            role = {
                "name": name.value,
                "description": description
            }
            new_role = crud.roleCRUD.create(db, obj_in=role)
            return new_role

    else:
        raise HTTPException(status_code=403, detail="User does not belong to the admin group that can create roles.")
