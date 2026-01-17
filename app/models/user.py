from uuid import uuid4
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from ..base import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(36), primary_key = True, default = lambda: str(uuid4()))
    name: Mapped[str] = mapped_column(String(100), nullable = False)
    email: Mapped[str] = mapped_column(String(255), unique = True, nullable = False)
    role: Mapped[str] = mapped_column(String(20), nullable = False)

    # auth will come later
