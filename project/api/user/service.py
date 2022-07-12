from project.lib.errors import ServerError
from project.api.book import Book
from project.api.transaction import transaction as transactionDB

from .interface import User

def get_user_by_id(token: str):
    return User.get_user_by_id(token)

def get_user_by_name(token: str):
    return User.get_user_by_name(userinfo=token)

def issued_books_service(user_id):
    books_id = User.get_issued_books_by_user(user_id)
    if books_id:
        books = []
        for book_id in books_id:
            book = Book.get_book_by_id(book_id)
            books.append({
                "book_id": book.book_id,
                "book_name": book.book_name,
                "author": book.author
            })
        return books
    return None




