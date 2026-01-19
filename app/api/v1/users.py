from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from sqlalchemy.orm import Session
from ...db.session import get_db
from ...schemas.user import UserCreate, UserRead
from ...services.user_service import UserService
from ..dependencies.deps import get_user_service
from app.api.dependencies.auth_deps import get_current_user
from ...models.user import User
from ..dependencies.rbac import require_role
from ...schemas.user import UserRole

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserRead)
def create_user(data: UserCreate, service: UserService = Depends(get_user_service), db: Session = Depends(get_db), _: User = Depends(require_role(UserRole.ADMIN))):
    try:
        return service.create_user(data, db)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[UserRead])
def list_users(service: UserService = Depends(get_user_service), db: Session = Depends(get_db), _: User = Depends(require_role(UserRole.ADMIN))):
    return service.list_users(db)

@router.get("/me", response_model=UserRead)
def me(current_user: User = Depends(get_current_user), service: UserService = Depends(get_user_service), db: Session = Depends(get_db)):
    user1 = service.get_user(current_user.id, db)
    if not user1:
        raise HTTPException(status_code=404, detail="User not found")
    return user1


@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: UUID, service: UserService = Depends(get_user_service), db: Session = Depends(get_db), _: User = Depends(require_role(UserRole.ADMIN))):
    user = service.get_user(user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
