from project.lib.errors import ServerError
from project.api.book import Book
from project.api.transaction import transaction

from .interface import User

def get_user_by_id(token: str):
    return User.get_user_by_id(token)

def get_user_by_name(token: str):
    return User.get_user_by_name(userinfo=token)

def issued_books_service(user_id):
    trans_id = User.get_issued_books_by_user(user_id)
    if trans_id:
        books = []
        for tran_id in trans_id:
            tran = transaction.get_transaction_by_id(tran_id)
            book = Book.get_book_by_id(tran.book_id)
            books.append({
                "book_id": book.book_id,
                "book_name": book.book_name,
                "author": book.author,
                "issue_date": tran.issue_date,
                "return_date": tran.return_date
            })
        return books
    return None




