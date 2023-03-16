from typing import TYPE_CHECKING, List

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base

if TYPE_CHECKING:
    from app.models import Step, Role


class User(Base):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True, index=True)
    username: str = Column(String, unique=True, index=True)
    firstName: str = Column(String)
    lastName: str = Column(String)
    email: str = Column(String, unique=True, index=True)
    is_active: bool = Column(Boolean, default=True)
    role_id: int = Column(Integer, ForeignKey("userroles.id"))

    role: "Role" = relationship("Role", foreign_keys=[role_id])
