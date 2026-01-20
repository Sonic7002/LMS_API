from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional

class BookCreate(BaseModel):
    title: str
    author: str
    total_copies: int = Field(gt=0)

class BookRead(BaseModel):
    id: UUID
    title: str
    author: str
    total_copies: int
    available_copies: int
    created_at: datetime

class BookPatch(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    total_copies: Optional[int] = None