from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import users, books, loans, auth, health
from app.db.base import Base
from app.db.session import engine
from app.db.session import SessionLocal
from app.models.user import User
from app.schemas.user import UserRole
import os

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Library Management System")

origins = os.getenv("ALLOWED_ORIGINS", "*")
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

INITIAL_ADMIN_EMAIL = os.getenv("INITIAL_ADMIN_EMAIL")
INITIAL_ADMIN_PASSWORD = os.getenv("INITIAL_ADMIN_PASSWORD")

if not INITIAL_ADMIN_EMAIL or not INITIAL_ADMIN_PASSWORD:
    raise RuntimeError("Missing initial admin email or password.")

@app.on_event("startup")
def create_initial_admin():
    db = SessionLocal()
    try:
        admin_exists = db.query(User).filter(User.role == UserRole.ADMIN).first()
        if not admin_exists:
            user = User(name = "Super Admin", email = INITIAL_ADMIN_EMAIL, role = UserRole.ADMIN)
            user.set_password(INITIAL_ADMIN_PASSWORD)
            db.add(user)
            db.commit()
    finally:
        db.close()

app.include_router(users.router, prefix="/api/v1")
app.include_router(books.router, prefix="/api/v1")
app.include_router(loans.router, prefix="/api/v1")
app.include_router(auth.router)
app.include_router(health.router)
