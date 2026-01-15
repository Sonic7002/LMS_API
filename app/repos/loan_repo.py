from uuid import UUID, uuid4
from datetime import datetime, timedelta
from ..schemas.loan import LoanStatus


class LoanRepo:
    def __init__(self):
        self.loans: dict[UUID, dict] = {}

    def create(self, user_id: UUID, book_id: UUID) -> dict:
        loan_id = uuid4()
        loan = {
            "id": loan_id,
            "user_id": user_id,
            "book_id": book_id,
            "issued_at": datetime.utcnow(),
            "due_at": datetime.utcnow() + timedelta(days=14),
            "returned_at": None,
            "status": LoanStatus.ISSUED,
        }
        self.loans[loan_id] = loan
        return loan

    def list_all(self) -> list[dict]:
        return list(self.loans.values())
