from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://pavanteja_sit722_part3_user:rYIO3yjWLxdhlFO9vBqX78q3JCCEdbYm@dpg-crsia80gph6c738tsb0g-a.oregon-postgres.render.com/pavanteja_sit722_part3" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
