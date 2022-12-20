from datetime import datetime  # noqa
from typing import TYPE_CHECKING

from sqlalchemy import Column, UniqueConstraint, ForeignKey, DateTime
from sqlalchemy.types import Integer, Enum, String
from app.db.database import Base
from sqlalchemy.orm import relationship
import enum

if TYPE_CHECKING:
    from app.models import User


class StatusEnum(str, enum.Enum):
    pending = "pending"
    in_progress = "in_progress"
    complete = "complete"


class Step(Base):
    __tablename__ = "steps"

    id: int = Column(Integer, primary_key=True, index=True)

    step_id: str = Column(String, nullable=False)
    substep_id: str = Column(String, nullable=False)
    status: str = Column(Enum(StatusEnum, name="_status_enum"))
    doc_uri: str = Column(String, nullable=True)
    status_updated_at: datetime = Column(DateTime, default=datetime.now())
    doc_updated_at: datetime = Column(DateTime, default=datetime.now())
    status_user_id: int = Column(Integer, ForeignKey("users.id"), nullable=True)
    doc_user_id: int = Column(Integer, ForeignKey("users.id"), nullable=True)

    __table_args__ = (
        UniqueConstraint("step_id", "substep_id", name="_step_substep_id"),
    )
    status_user: "User" = relationship("User", foreign_keys=[status_user_id])
    doc_user: "User" = relationship("User", foreign_keys=[doc_user_id])
