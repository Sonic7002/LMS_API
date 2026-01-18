from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from sqlalchemy.orm import Session
from ...db.session import get_db
from ...schemas.user import UserCreate, UserRead
from ...services.user_service import UserService
from ..deps import get_user_service
from app.api.auth_deps import get_current_user

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserRead)
def create_user(data: UserCreate, service: UserService = Depends(get_user_service), db: Session = Depends(get_db)):
    return service.create_user(data, db)

@router.get("/", response_model=list[UserRead])
def list_users(service: UserService = Depends(get_user_service), db: Session = Depends(get_db)):
    return service.list_users(db)

@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: UUID, service: UserService = Depends(get_user_service), db: Session = Depends(get_db)):
    user = service.get_user(user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/me")
def me(user = Depends(get_current_user)):
    return {
        "id": user.id,
        "email": user.email,
    }
