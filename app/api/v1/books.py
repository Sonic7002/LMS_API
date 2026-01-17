from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID

from app.schemas.book import BookCreate, BookRead
from app.services.book_service import BookService
from app.api.deps import get_book_service

router = APIRouter(prefix="/books", tags=["books"])


@router.post("/", response_model=BookRead)
def create_book(data: BookCreate, service: BookService = Depends(get_book_service)):
    return service.create_book(data)

@router.get("/", response_model=list[BookRead])
def list_books(service: BookService = Depends(get_book_service)):
    return service.list_books()

@router.get("/{book_id}", response_model=BookRead)
def get_book(book_id: UUID, service: BookService = Depends(get_book_service)):
    book = service.get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
