from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, Field

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
