from uuid import UUID
from ..repos.book_repo import BookRepo
from ..schemas.book import BookCreate, BookPatch
from ..models.book import Book
from sqlalchemy.orm import Session
class BookService:
    def __init__(self, repo: BookRepo):
        self.repo = repo

    def create_book(self, data: BookCreate, db: Session) -> Book:
        return self.repo.create(db, data)

    def get_book(self, book_id: UUID, db: Session) -> Book | None:
        return self.repo.get_by_id(db, book_id)

    def list_books(self, db: Session) -> list[Book]:
        return self.repo.list_all(db)

    def edit_book(self, book_id: UUID, data: BookPatch, db: Session) -> Book | None:
        book = self.repo.get_by_id(db, book_id)
        updates = data.model_dump(exclude_unset=True)

        if "total_copies" in updates:
            if updates["total_copies"] < book.available_copies:
                raise ValueError("total_copies cannot be less than currently borrowed copies")

        for field, value in updates.items():
            setattr(book, field, value)

        return self.repo.save(db, book)
    
    def delete_book(self, book_id: UUID, db: Session) -> Book | None:
        return self.repo.delete(db, book_id)
