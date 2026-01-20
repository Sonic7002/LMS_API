from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from sqlalchemy.orm import Session
from ...db.session import get_db
from app.services.loan_service import LoanService
from app.api.dependencies.deps import get_loan_service
from ...models.user import User
from ..dependencies.rbac import require_role
from ...schemas.user import UserRole
from ...schemas.loan import LoanRead

router = APIRouter(prefix="/loans", tags=["loans"])

@router.post("/issue", response_model=LoanRead)
def issue_book(user_id: UUID, book_id: UUID, service: LoanService = Depends(get_loan_service), db: Session = Depends(get_db), _: User = Depends(require_role(UserRole.LIBRARIAN))):
    try:
        return service.issue_book(user_id, book_id, db)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/return/{loan_id}", response_model=LoanRead)
def return_book(loan_id: UUID, service: LoanService = Depends(get_loan_service), db: Session = Depends(get_db), _: User = Depends(require_role(UserRole.LIBRARIAN))):
    try:
        return service.return_book(loan_id, db)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/me",response_model=LoanRead)
def list_user_loans(service: LoanService = Depends(get_loan_service), db: Session = Depends(get_db), current_user: User = Depends(require_role(UserRole.ADMIN, UserRole.LIBRARIAN))):
    return service.list_loans_for_user(current_user.id, db)

@router.get("/", response_model=LoanRead)
def list_loans(service: LoanService = Depends(get_loan_service), db: Session = Depends(get_db), _: User = Depends(require_role(UserRole.ADMIN, UserRole.LIBRARIAN))):
    return service.list_loans(db)
