# health route

from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["health"])

@router.get("/health")
def health():
    """always returns 200 if running"""
    return {"status": "ok"}