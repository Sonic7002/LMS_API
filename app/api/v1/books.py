from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from sqlalchemy.orm import Session
from ...db.session import get_db
from app.schemas.book import BookCreate, BookRead
from app.services.book_service import BookService
from app.api.dependencies.deps import get_book_service
from ...models.user import User
from ..dependencies.rbac import require_role
from ...schemas.user import UserRole

router = APIRouter(prefix="/books", tags=["books"])


@router.post("/", response_model=BookRead)
def create_book(data: BookCreate, service: BookService = Depends(get_book_service), db: Session = Depends(get_db), _: User = Depends(require_role(UserRole.ADMIN))):
    return service.create_book(data, db)

@router.get("/", response_model=list[BookRead])
def list_books(service: BookService = Depends(get_book_service), db: Session = Depends(get_db)):
    return service.list_books(db)

@router.get("/{book_id}", response_model=BookRead)
def get_book(book_id: UUID, service: BookService = Depends(get_book_service), db: Session = Depends(get_db)):
    book = service.get_book(book_id, db)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
