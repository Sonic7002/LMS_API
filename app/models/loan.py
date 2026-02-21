from uuid import uuid4, UUID as PyUUID
from datetime import datetime
from sqlalchemy import String, DateTime, ForeignKey, func 
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from ..db.base import Base

class Loan(Base):
    __tablename__ = "loans"

    id: Mapped[PyUUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id: Mapped[PyUUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    book_id: Mapped[PyUUID] = mapped_column(ForeignKey("books.id"), nullable=False)
    status: Mapped[str] = mapped_column(String(20), nullable=False)
    issued_at: Mapped[datetime] = mapped_column(DateTime(timezone = True), server_default=func.now(), nullable = False)
    due_at: Mapped[datetime] = mapped_column(DateTime(timezone = True), nullable = False)
    returned_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))

    user = relationship("User")
    book = relationship("Book")
