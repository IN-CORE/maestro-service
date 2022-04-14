from sqlalchemy import Column, Integer, Enum

from app.db.database import Base
import enum


class StatusEnum(enum.Enum):
    pending = "Pending"
    in_progress = "In-Progress"
    complete = "Complete"


class Step(Base):
    __tablename__ = "steps"

    step_id = Column(Integer, primary_key=True, index=True)
    substep_id = Column(Integer, primary_key=True, index=True)
    status = Column(Enum(StatusEnum))
