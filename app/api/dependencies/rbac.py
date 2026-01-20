from fastapi import Depends, HTTPException, status
from app.models.user import User
from app.api.dependencies.auth_deps import get_current_user
from app.schemas.user import UserRole

def require_role(*allowed_roles: UserRole):
    def role_checker(current_user: User = Depends(get_current_user)):
        if current_user.role not in allowed_roles or current_user.is_active == False:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")
        return current_user
    return role_checker
