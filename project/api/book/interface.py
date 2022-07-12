from dataclasses import dataclass
from typing import Dict, Any

from project.extensions import db

from .model import Book as BookDB

@dataclass
class Book:
    book_id: str
    book_name: str
    author: str
    tag: str
    total_copies: int
    available_copies: int

    @classmethod
    def instance_creator(cls, book_db: BookDB):
        return cls(
            book_id = book_db.book_id,
            book_name = book_db.book_name,
            author = book_db.author,
            tag = book_db.tag,
            total_copies = book_db.total_copies,
            available_copies = book_db.available_copies
        )

    @classmethod
    def get_book_by_id(cls, book_id):
        book = BookDB.get_first({"book_id": book_id})
        if book:
            return cls.instance_creator(book_db=book)
        return None
    
    @classmethod
    def get_book_by_name(cls, book_name):
        book_db: BookDB = BookDB.get_first({"book_name": book_name})
        if book_db:
            return cls.instance_creator(book_db)
        return None

    @classmethod
    def add_book(cls, bookinfo: Dict[str, Any]):
        book_db = BookDB(
            book_name = bookinfo["book_name"],
            author = bookinfo["author"],
            tag = bookinfo["tag"],
            total_copies = bookinfo["total_copies"],
            available_copies = bookinfo["total_copies"]
        )
        book_db.create()
        if book_db:
            return cls.instance_creator(book_db)
    
    @classmethod
    def delete_book_by_id(cls, book_id):
        book_db: BookDB = BookDB.get_first({"book_id": book_id})
        if book_db:
            book_db.delete()
            return True
        return False
    
    @classmethod
    def update_book(cls, bookinfo: Dict[str, Any]):
        book_db: BookDB = BookDB.get_first({"book_id": bookinfo["book_id"]})
        if book_db:
            book_db = book_db.update(**bookinfo)
            return cls.instance_creator(book_db)
        return None
    
    @classmethod
    def get_all_books(cls):
        books = BookDB.get_all()
        if books:
            return [cls.instance_creator(book_db) for book_db in books]
        return None
