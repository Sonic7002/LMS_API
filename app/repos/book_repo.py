from uuid import UUID, uuid4
from datetime import datetime
from ..schemas.book import BookCreate


class BookRepo:
    def __init__(self):
        self.books: dict[UUID, dict] = {}

    def create(self, data: BookCreate) -> dict:
        book_id = uuid4()
        book = {
            "id": book_id,
            "title": data.title,
            "author": data.author,
            "isbn": data.isbn,
            "total_copies": data.total_copies,
            "available_copies": data.total_copies,
            "created_at": datetime.utcnow(),
        }
        self.books[book_id] = book
        return book

    def get_by_id(self, book_id: UUID) -> dict | None:
        return self.books.get(book_id)

    def list_all(self) -> list[dict]:
        return list(self.books.values())
