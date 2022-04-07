from sqlalchemy.orm import Session

from app.db import schemas
from app.models import User, Role


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = User(username=user.username, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_roles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Role).offset(skip).limit(limit).all()


def create_user_role(db: Session, role: schemas.RoleCreate, user_id: int):
    db_role = Role(**role.dict(), user_id=user_id)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role
