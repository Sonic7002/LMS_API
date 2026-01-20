from uuid import UUID
from sqlalchemy.orm import Session
from ..models.book import Book
from ..schemas.book import BookCreate, BookPatch

class BookRepo:
    def create(self, db: Session,  data: BookCreate) -> Book:
        book = Book(title = data.title, author = data.author, total_copies = data.total_copies)
        book.available_copies = data.total_copies
        db.add(book)
        db.commit()
        db.refresh(book)
        return book

    def get_by_id(self, db: Session, book_id: UUID) -> Book | None:
        return db.query(Book).filter(Book.id == str(book_id)).first()

    def list_all(self, db: Session) -> list[Book]:
        return db.query(Book).all()

    def save(self, db: Session, book: Book) -> Book | None:
        db.commit()
        db.refresh(book)
        return book

    def delete(self, db: Session, book_id: UUID) -> Book | None:
        book = db.query(Book).filter(Book.id == str(book_id)).first()
        db.delete(book)
        db.commit()
        return book
