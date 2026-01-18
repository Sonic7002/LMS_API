from uuid import UUID
from sqlalchemy.orm import Session
from ..models.user import User
from ..repos.user_repo import UserRepo
from ..schemas.user import UserCreate

class UserService:

    def _to_dict(self, data: User) -> dict:
        return {
            "id": data.id,
            "name": data.name,
            "email": data.email,
            "role": data.role,
            "is_active": data.is_active,
            "created_at": data.created_at
        }
    
    def __init__(self, repo: UserRepo):
        self.repo = repo

    def create_user(self, data: UserCreate, db: Session) -> dict:
        return self._to_dict(self.repo.create(db, data))

    def get_user(self, user_id: UUID, db: Session) -> dict | None:
        return self._to_dict(self.repo.get_by_id(db, user_id))

    def list_users(self, db: Session) -> list[dict]:
        users = self.repo.list_all(db)
        return [self._to_dict(user) for user in users]
