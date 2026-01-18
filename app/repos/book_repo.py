from uuid import UUID
from sqlalchemy.orm import Session
from ..models.book import Book
from datetime import datetime
from ..schemas.book import BookCreate

class BookRepo:
    def create(self, db: Session,  data: BookCreate) -> Book:
        book = Book(title = data.title, author = data.author, total_copies = data.total_copies)
        db.add(book)
        db.commit()
        db.refresh(book)
        return book

    def get_by_id(self, db: Session, book_id: UUID) -> Book | None:
        return db.query(Book).filer_by(Book.id == str(book_id)).first()

    def list_all(self, db: Session) -> list[Book]:
        return db.query(Book).all()
