from sqlalchemy import Column, JSON, String

from app.db.database import Base


class RetrofitStrategyDetails(Base):
    __tablename__ = "rsdetails"

    dataset_id: str = Column(String, primary_key=True, index=True)
    total = Column(JSON)
    by_rule = Column(JSON)
    rules = Column(JSON)
    retrofits = Column(JSON)
    rsDetailsLayerId: str = Column(String)

