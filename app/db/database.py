from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# create a file called session.py and load all env variables there. DB settings should also be part of env
SQLALCHEMY_DATABASE_URL = "postgresql://maestro:maestro@localhost:5432/maestro"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
