import json

from fastapi import APIRouter, Depends, Header, HTTPException
from typing import Union, Any

from app import crud
from app.db import schemas
from app.models.Role import RoleEnum
from sqlalchemy.orm import Session

from app.db.database import get_db

router = APIRouter()


@router.get("", response_model=list[schemas.Role])
def read_roles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> Any:
    roles = crud.roleCRUD.get_multi(db, skip=skip, limit=limit)
    return roles


@router.post("", response_model=schemas.Role)
def create_roles(name: RoleEnum, description: str, x_auth_usergroup: Union[str, None] = Header(None),  db: Session = Depends(get_db)) -> Any:
    if x_auth_usergroup is not None:
        try:
            groups = json.loads(x_auth_usergroup)
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
