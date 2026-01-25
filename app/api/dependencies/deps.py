# this file contains dependecy methods for routes
# it injects the repos in services and returns them

from app.repos.user_repo import UserRepo
from app.repos.book_repo import BookRepo
from app.repos.loan_repo import LoanRepo
from app.services.user_service import UserService
from app.services.book_service import BookService
from app.services.loan_service import LoanService
user_repo = UserRepo()
book_repo = BookRepo()
loan_repo = LoanRepo()

def get_user_service() -> UserService:
    """initialise user service class and return it"""
    return UserService(user_repo)

def get_book_service() -> BookService:
    """initialise book service class and return it"""
    return BookService(book_repo)

def get_loan_service() -> LoanService:
    """initialise loan service class and return it"""
    return LoanService(loan_repo, book_repo, user_repo)
