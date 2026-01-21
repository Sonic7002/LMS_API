from uuid import UUID
from ..schemas.loan import LoanStatus
from sqlalchemy.orm import Session
from ..models.loan import Loan

class LoanRepo:
    def create(self, db: Session, user_id: UUID, book_id: UUID) -> Loan:
        loan = Loan(user_id = str(user_id), book_id = str(book_id), status = LoanStatus.ISSUED)
        db.add(loan)
        db.commit()
        db.refresh(loan)
        return loan

    def get_by_id(self, db: Session, loan_id: UUID) -> Loan | None:
        return db.query(Loan).filter(Loan.id == str(loan_id)).first()

    def list_all(self, db: Session) -> list[Loan]:
        return db.query(Loan).all()
    
    def list_for_user(self, user_id: UUID, db:Session) -> list[Loan]:
        return db.query(Loan).filter(Loan.user_id == str(user_id)).all()
    
    def save(self, db: Session, loan: Loan):
        db.commit()
        db.refresh(loan)
        return loan
