from uuid import uuid4
from datetime import datetime
from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db.base import Base

class Loan(Base):
    __tablename__ = "loans"

    id: Mapped[str] = mapped_column(String(36), primary_key = True, default = lambda: str(uuid4()))
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), nullable = False)
    book_id: Mapped[str] = mapped_column(ForeignKey("books.id"), nullable = False)
    status: Mapped[str] = mapped_column(String(20), nullable=False)
    issued_at: Mapped[datetime] = mapped_column(DateTime(timezone = True), default = datetime.utcnow, nullable = False)
    due_at: Mapped[datetime] = mapped_column(DateTime(timezone = True), nullable = False)
    returned_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))

    user = relationship("User")
    book = relationship("Book")
