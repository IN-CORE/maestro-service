from sqlalchemy import Column, JSON, String

from app.db.database import Base


class RetrofitStrategyDetails(Base):
    """
       {
       "total": {
           "num_bldg": 3283,
           "num_bldg_no_cost": 42,
           "cost": 117260721.43
       },
       "by_rule": {
           "0": {
               "num_bldg": 3191,
               "num_bldg_no_cost": 40,
               "cost": 94393478.73
           },
           "1": {
               "num_bldg": 90,
               "num_bldg_no_cost": 0,
               "cost": 22867242.7
           },
           "2": {
               "num_bldg": 2,
               "num_bldg_no_cost": 2,
               "cost": 0
               }
           }
       }
       """
    __tablename__ = "rsdetails"

    dataset_id: str = Column(String, primary_key=True, index=True)
    total = Column(JSON)
    by_rule = Column(JSON)

