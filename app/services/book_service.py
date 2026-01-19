from uuid import UUID
from ..repos.book_repo import BookRepo
from ..schemas.book import BookCreate
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
