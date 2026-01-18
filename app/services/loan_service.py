from uuid import UUID
from datetime import datetime
from ..repos.loan_repo import LoanRepo
from ..repos.book_repo import BookRepo
from ..repos.user_repo import UserRepo
from ..schemas.loan import LoanStatus
from ..models.loan import Loan
from sqlalchemy.orm import Session

class LoanService:
    def _to_dict(self, data: Loan):
        return {
            "id": data.id,
            "user_id": data.user_id,
            "book_id": data.book_id,
            "issued_at": data.issued_at,
            "returned_at": data.returned_at,
            "status": data.status
        }

    def __init__(self, loan_repo: LoanRepo, book_repo: BookRepo, user_repo: UserRepo):
        self.loan_repo = loan_repo
        self.book_repo = book_repo
        self.user_repo = user_repo

    def issue_book(self, user_id: UUID, book_id: UUID, db: Session) -> dict:
        user = self.user_repo.get_by_id(db, user_id)
        book = self.book_repo.get_by_id(db, book_id)

        if not user or not book:
            raise ValueError("User or Book not found")

        if book["available_copies"] <= 0:
            raise ValueError("No copies available")

        # prevent duplicate active loan
        for loan in self.loan_repo.list_all(db):
            if (loan.user_id == user_id and loan.book_id == book_id and loan.status == LoanStatus.ISSUED):
                raise ValueError("Book already issued to user")

        book.available_copies -= 1
        return self._to_dict(self.loan_repo.create(db, user_id, book_id))

    def return_book(self, loan_id: UUID, db: Session) -> dict:
        loan = self.loan_repo.get_by_id(db, loan_id)

        if not loan or loan.status != LoanStatus.ISSUED:
            raise ValueError("Invalid loan")

        book = self.book_repo.get_by_id(db, loan.book_id)
        book.available_copies += 1

        loan.status = LoanStatus.RETURNED
        loan.returned_at = datetime.utcnow()

        return self._to_dict(loan)

    def list_loans(self, db: Session) -> list[dict]:
        return self.loan_repo.list_all(db)

    # not still implemented in routes
    def list_loans_for_user(self, user_id: UUID, db: Session) -> list[dict]:
        return [self._to_dict(loan) for loan in self.loan_repo.list_all(db) if loan.user_id == str(user_id)]
