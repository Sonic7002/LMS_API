from uuid import UUID, uuid4
from datetime import datetime
from ..schemas.user import UserCreate


class UserRepo:
    def __init__(self):
        self.users: dict[UUID, dict] = {}

    def create(self, data: UserCreate) -> dict:
        user_id = uuid4()
        user = {
            "id": user_id,
            "name": data.name,
            "email": data.email,
            "hashed_password": "hashed",  # TEMP
            "role": data.role,
            "is_active": True,
            "created_at": datetime.utcnow(),
        }
        self.users[user_id] = user
        return user

    def get_by_id(self, user_id: UUID) -> dict | None:
        return self.users.get(user_id)

    def list_all(self) -> list[dict]:
        return list(self.users.values())
