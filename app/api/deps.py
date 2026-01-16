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
    return UserService(user_repo)


def get_book_service() -> BookService:
    return BookService(book_repo)


def get_loan_service() -> LoanService:
    return LoanService(
        loan_repo=loan_repo,
        book_repo=book_repo,
        user_repo=user_repo,
    )
