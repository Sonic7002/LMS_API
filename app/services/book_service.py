from uuid import UUID
from ..repos.book_repo import BookRepo
from ..schemas.book import BookCreate
from ..models.book import Book

class BookService:
    def _to_dict(data: Book) -> dict:
        return{
            "id": data.id,
            "title": data.title,
            "author": data.author,
            "total_copies": data.total_copies,
            "available_copies": data.available_copies,
            "created_at": data.created_at
        }

    def __init__(self, repo: BookRepo):
        self.repo = repo

    def create_book(self, data: BookCreate) -> dict:
        return self._to_dict(self.repo.create(data))

    def get_book(self, book_id: UUID) -> dict | None:
        return self._to_dict(self.repo.get_by_id(book_id))

    def list_books(self) -> list[dict]:
        return self._to_dict(self.repo.list_all())
