from uuid import UUID
from ..schemas.loan import LoanStatus
from sqlalchemy.orm import Session
from ..models.loan import Loan

class LoanRepo:
    def create(self, db: Session, user_id: UUID, book_id: UUID) -> Loan:
        loan = Loan(user_id = str(user_id), book_id = str(book_id), status = LoanStatus.ISSUED)
        return loan

    def get_by_id(self, db: Session, loan_id: UUID) -> Loan | None:
        db.query(Loan).filter_by(Loan.id == str(loan_id)).first()

    def list_all(self, db: Session) -> list[Loan]:
        return db.query(Loan).all()
