from typing import TYPE_CHECKING, List
from sqlalchemy.types import Enum
import enum

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base

if TYPE_CHECKING:
    from app.models import User


class RoleEnum(str, enum.Enum):
    leader = "leader"
    member = "member"


class Role(Base):
    __tablename__ = "userroles"

    id: str = Column(Integer, primary_key=True, index=True)
    name: str = Column(Enum(RoleEnum, name="_role_enum"), unique=True, index=True)
    description: str = Column(String)
