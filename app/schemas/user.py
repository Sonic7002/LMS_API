from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, field_validator, ValidationInfo
from enum import Enum
from typing import Optional

class UserRole(str, Enum):
    ADMIN = "ADMIN"
    LIBRARIAN = "LIBRARIAN"
    MEMBER = "MEMBER"

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)     # bcrypt byte limit 72
    role: UserRole

    @field_validator("name")
    @classmethod
    def not_empty(cls, v: str, info: ValidationInfo):
        if not v.strip():
            raise ValueError(f"{info.field_name} must not be empty")
        return v

class UserRead(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    role: UserRole
    is_active: bool
    created_at: datetime

class UserPatch(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

    @field_validator("name")
    @classmethod
    def not_empty(cls, v: str, info: ValidationInfo):
        if not v.strip():
            raise ValueError(f"{info.field_name} must not be empty")
        return v
