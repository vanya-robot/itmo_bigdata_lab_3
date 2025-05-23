from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.config import settings
import time

Base = declarative_base()
engine = None
SessionLocal = None

def init_db_connection():
    global engine, SessionLocal
    if engine is None:
        engine = create_engine(settings.get_db_url())
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    if engine is None:
        init_db_connection()
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()