from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from ...schemas.user import UserCreate, UserRead
from ...services.user_service import UserService
from ..deps import get_user_service
from app.api.auth_deps import get_current_user

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserRead)
def create_user(data: UserCreate, service: UserService = Depends(get_user_service)):
    return service.create_user(data)

@router.get("/", response_model=list[UserRead])
def list_users(service: UserService = Depends(get_user_service)):
    return service.list_users()

@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: UUID, service: UserService = Depends(get_user_service)):
    user = service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/me")
def me(user = Depends(get_current_user)):
    return {
        "id": user.id,
        "email": user.email,
    }
