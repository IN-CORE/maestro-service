from fastapi import HTTPException

from app.crud.base import CRUDBase
from app.db.schemas import UserCreate, UserUpdate
from app.models import User, Role
from sqlalchemy.orm import Session


class UserCRUD(
    CRUDBase[User, UserCreate, UserUpdate]
):

    def get_user_by_email(self, db: Session, email: str) -> User:
        return db.query(User).filter(User.email == email).first()

    def get_user_by_username(self, db: Session, username: str):
        return db.query(User).filter(User.username == username).first()

    def attach_user_role(self, db: Session, user_id: int, role_id: int):
        db_user = db.query(User).filter(User.id == user_id).first()
        if db_user is None:
            raise HTTPException(status_code=404, detail=f"User id: {user_id} not found")
        db_role = db.query(Role).filter(Role.id == role_id).first()
        if db_role is None:
            raise HTTPException(status_code=404, detail=f"Role id: {role_id} not found")
        db_user.role = db_role
        db.commit()
        db.refresh(db_user)

        return db_user


userCRUD = UserCRUD(User)
