from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from sqlalchemy.orm import Session
from ...db.session import get_db
from ...schemas.user import UserCreate, UserRead, UserPatch, UserRole
from ...services.user_service import UserService
from ..dependencies.deps import get_user_service
from app.api.dependencies.auth_deps import get_current_user
from ...models.user import User
from ..dependencies.rbac import require_role

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
    user = service.get_user(current_user.id, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.patch("/deactivate/{user_id}", response_model=UserRead)
def deactivate(user_id: UUID, service: UserService = Depends(get_user_service), db: Session = Depends(get_db), current_user: User = Depends(require_role(UserRole.ADMIN))):
    try:
        if current_user.id == str(id):
            raise HTTPException(status_code=400, detail= "cannot deactivate self")
        user = service.deactivate(user_id,db)
        if not user:
            raise HTTPException(status_code=404, detail="Invlid user ID")
        return user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.patch("/activate/{user_id}", response_model=UserRead)
def deactivate(user_id: UUID, service: UserService = Depends(get_user_service), db: Session = Depends(get_db), _: User = Depends(require_role(UserRole.ADMIN))):
    try:
        user = service.activate(user_id,db)
        if not user:
            raise HTTPException(status_code=404, detail="Invlid user ID")
        return user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.patch("/{user_id}", response_model=UserRead)
def edit_user(user_id: UUID, data: UserPatch,service: UserService = Depends(get_user_service), db: Session = Depends(get_db), _:User = Depends(require_role(UserRole.ADMIN, UserRole.MEMBER, UserRole.LIBRARIAN))):
    try:
        user = service.edit_user(user_id, data, db)
        if not user:
            raise HTTPException(status_code=404, detail="Invlid user ID")
        return user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: UUID, service: UserService = Depends(get_user_service), db: Session = Depends(get_db), _: User = Depends(require_role(UserRole.ADMIN))):
    user = service.get_user(user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
