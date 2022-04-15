from sqlalchemy import Column, Integer, Enum, String, UniqueConstraint

from app.db.database import Base
import enum


class StatusEnum(enum.Enum):
    pending = "Pending"
    in_progress = "In-Progress"
    complete = "Complete"


class Step(Base):
    __tablename__ = "steps"

    id = Column(Integer, primary_key=True)

    step_id = Column(String, nullable=False)
    substep_id = Column(String, nullable=False)

    __table_args__ = (UniqueConstraint("step_id", 'substep_id', name='_step_substep_id'),)
    status = Column(Enum(StatusEnum))
