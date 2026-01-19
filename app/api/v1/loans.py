from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from sqlalchemy.orm import Session
from ...db.session import get_db
from app.services.loan_service import LoanService
from app.api.dependencies.deps import get_loan_service
from ...models.user import User
from ..dependencies.rbac import require_role
from ...schemas.user import UserRole

router = APIRouter(prefix="/loans", tags=["loans"])

@router.post("/issue")
def issue_book(user_id: UUID, book_id: UUID, service: LoanService = Depends(get_loan_service), db: Session = Depends(get_db), _: User = Depends(require_role(UserRole.LIBRARIAN))):
    try:
        return service.issue_book(user_id, book_id, db)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/{loan_id}/return")
def return_book(loan_id: UUID, service: LoanService = Depends(get_loan_service), db: Session = Depends(get_db), _: User = Depends(require_role(UserRole.LIBRARIAN))):
    try:
        return service.return_book(loan_id, db)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/")
def list_loans(service: LoanService = Depends(get_loan_service), db: Session = Depends(get_db), _: User = Depends(require_role(UserRole.ADMIN, UserRole.LIBRARIAN))):
    return service.list_loans(db)
