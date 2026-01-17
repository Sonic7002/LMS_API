from uuid import UUID
from ..repos.user_repo import UserRepo
from ..schemas.user import UserCreate

class UserService:
    def __init__(self, repo: UserRepo):
        self.repo = repo

    def create_user(self, data: UserCreate) -> dict:
        return self.repo.create(data)

    def get_user(self, user_id: UUID) -> dict | None:
        return self.repo.get_by_id(user_id)

    def list_users(self) -> list[dict]:
        return self.repo.list_all()
