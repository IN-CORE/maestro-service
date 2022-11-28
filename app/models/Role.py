from sqlalchemy.types import Enum

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base


class Role(Base):
    __tablename__ = "userroles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Enum("leader", "member", name="_role_enum"), unique=True, index=True)
    description = Column(String)

