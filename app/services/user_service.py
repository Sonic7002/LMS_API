from uuid import UUID
from sqlalchemy.orm import Session
from ..models.user import User
from ..repos.user_repo import UserRepo
from ..schemas.user import UserCreate

class UserService:
    def __init__(self, repo: UserRepo):
        self.repo = repo

    def create_user(self, data: UserCreate, db: Session) -> User:
        user = self.repo.create(db, data)
        if user:
            return user
        raise ValueError("email already exists")

    def get_user(self, user_id: UUID, db: Session) -> dict | None:
        return self.repo.get_by_id(db, user_id)

    def list_users(self, db: Session) -> list[dict]:
        return self.repo.list_all(db)
