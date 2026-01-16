from fastapi import FastAPI
from app.api.v1 import users, books, loans
from app.db.base import Base
from app.db.session import engine

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Library Management System")

app.include_router(users.router, prefix="/api/v1")
app.include_router(books.router, prefix="/api/v1")
app.include_router(loans.router, prefix="/api/v1")
