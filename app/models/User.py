from typing import TYPE_CHECKING, List

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base

if TYPE_CHECKING:
    from app.models import Step


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    firstName = Column(String)
    lastName = Column(String)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)

    role_id = Column(Integer, ForeignKey("userroles.id"))

    role = relationship("Role", back_populates="user_role")
    step_user: List["Step"] = relationship("Step", back_populates="user")
