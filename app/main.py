from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app.crud import crud
from app.db import schemas

from app.models import Role, User
from app.db.database import SessionLocal

app = FastAPI(title="Maestro API")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def index():
    return {"message": "Welcome to Maestro service"}


# TODO: Move each of these routes as separate files/classes in "routes" folder. Use fastapi.APIRouter

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/roles/", response_model=schemas.Role)
def create_role_for_user(
        user_id: int, role: schemas.RoleCreate, db: Session = Depends(get_db)
):
    return crud.create_user_role(db=db, role=role, user_id=user_id)


@app.get("/roles/", response_model=list[schemas.Role])
def read_roles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    roles = crud.get_roles(db, skip=skip, limit=limit)
    return roles
