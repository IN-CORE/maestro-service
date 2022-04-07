from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base


class Role(Base):
    __tablename__ = "userroles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    user_role = relationship("User", back_populates="roles")


