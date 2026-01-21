from enum import Enum
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel

class LoanStatus(str, Enum):
    ISSUED = "ISSUED"
    RETURNED = "RETURNED"
    OVERDUE = "OVERDUE"

class LoanRead(BaseModel):
    id: UUID
    user_id: UUID
    book_id: UUID
    issued_at: datetime
    due_at: datetime
    returned_at: datetime | None
    status: LoanStatus
