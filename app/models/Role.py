from sqlalchemy.types import Enum
import enum

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base


class RoleEnum(str, enum.Enum):
    leader = "leader"
    member = "member"

class Role(Base):
    __tablename__ = "userroles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Enum(RoleEnum, name="_role_enum"), unique=True, index=True)
    description = Column(String)

    user_role = relationship("User", back_populates="role")

