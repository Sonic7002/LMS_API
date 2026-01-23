from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, Field, field_validator, ValidationInfo
from typing import Optional

class BookCreate(BaseModel):
    title: str
    author: str
    total_copies: int = Field(gt=0)

    @field_validator("title", "author")
    @classmethod
    def not_empty(cls, v: str, info: ValidationInfo):
        if not v.strip():
            raise ValueError(f"{info.field_name} must not be empty")
        return v

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
    total_copies: Optional[int] = Field(gt=0, default=None)

    @field_validator("title", "author")
    @classmethod
    def not_empty(cls, v: str, info: ValidationInfo):
        if v is None:
            pass 
        elif not v.strip():
            raise ValueError(f"{info.field_name} must not be empty")
        return v