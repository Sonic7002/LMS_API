from uuid import UUID
from ..repos.book_repo import BookRepo
from ..schemas.book import BookCreate


class BookService:
    def __init__(self, repo: BookRepo):
        self.repo = repo

    def create_book(self, data: BookCreate) -> dict:
        return self.repo.create(data)

    def get_book(self, book_id: UUID) -> dict | None:
        return self.repo.get_by_id(book_id)

    def list_books(self) -> list[dict]:
        return self.repo.list_all()
