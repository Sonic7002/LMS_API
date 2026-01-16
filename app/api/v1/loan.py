from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID

from app.services.loan_service import LoanService
from app.api.deps import get_loan_service

router = APIRouter(prefix="/loans", tags=["loans"])


@router.post("/issue")
def issue_book(
    user_id: UUID,
    book_id: UUID,
    service: LoanService = Depends(get_loan_service),
):
    try:
        return service.issue_book(user_id, book_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/{loan_id}/return")
def return_book(
    loan_id: UUID,
    service: LoanService = Depends(get_loan_service),
):
    try:
        return service.return_book(loan_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/")
def list_loans(
    service: LoanService = Depends(get_loan_service),
):
    return service.list_loans()
