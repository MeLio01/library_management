from flask import request

from project.lib.errors import ServerError

from .model import Book as BookDB
from .interface import Book

def get_book_by_id(token: str):
    return Book.get_book_by_id(token)

def get_book_by_name(token: str):
    return Book.get_book_by_name(book_name=token)