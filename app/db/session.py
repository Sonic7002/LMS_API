from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator

DATABASE_URL = "sqlite:///./lms.db"

engine = create_engine(
    DATABASE_URL,
    echo=False,          # turn True when debugging SQL
    future=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
