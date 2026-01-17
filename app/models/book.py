from uuid import uuid4
from datetime import datetime
from sqlalchemy import String, Integer, Datetime
from sqlalchemy.orm import Mapped, mapped_column
from ..db.base import Base

class Book(Base):
    __tablename__ = "books"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default = lambda: str(uuid4()))
    title: Mapped[str] = mapped_column(String(200), nullable = False)
    author: Mapped[str] = mapped_column(String(200), nullable = False)
    total_copies: Mapped[int] = mapped_column(Integer, nullable = False)
    available_copies: Mapped[int] = mapped_column(Integer, nullable = False)
    created_at: Mapped[datetime] = mapped_column(Datetime, default = datetime.utcnow(), nullable = False)
