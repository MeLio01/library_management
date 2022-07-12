import os
from urllib import response
from flask import redirect, Blueprint, request, jsonify

from .interface import Book
from .service import get_book_by_id, get_book_by_name
from .schema import book_profile_schema, book_id_schema, book_out_schema

from project.lib.errors import BadRequest, BaseError

book_blueprint = Blueprint("book", __name__)

def add_book():
    auth: str = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization header invalid")
    data = book_profile_schema.load(request.json)
    book = Book.add_book(data)
    response = book_out_schema.dump(book)
    return response, 200

def delete_book():
    auth: str = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization header invalid")
    data = book_id_schema.load(request.json)
    delete = Book.delete_book_by_id(data["book_id"])
    if delete == False:
        raise BadRequest("Book id invalid", 400)
    return True

def update_book():
    auth: str = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization header invalid")
    data = book_out_schema.load(request.json)
    book = Book.update_book(data)
    if book == None:
        raise BadRequest("Book id invalid", 400)
    response = jsonify(book_out_schema.dump(book))
    return response, 200

def book_by_id():
    auth: str = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization header invalid")
    data = book_id_schema.load(request.json)
    book = get_book_by_id(data["book_id"])
    if book == None:
        raise BadRequest("Book id invalid", 400)
    response = jsonify(book_out_schema.dump(book))
    return response, 200

def book_by_name():
    auth: str = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization header invalid")
    data = book_profile_schema.load(request.json)
    book = get_book_by_name(data["book_name "])
    if book == None:
        raise BadRequest("Book name invalid", 400)
    response = jsonify(book_out_schema.dump(book))
    return response, 200

def get_all_books():
    auth: str = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization header invalid")
    books = Book.get_all_books()
    return {"Books": books}, 200



book_blueprint.add_url_rule("book/add_book", "add_book", add_book, methods=["POST"])
book_blueprint.add_url_rule("book/delete_book", "delete_book", delete_book, methods=["DELETE"])
book_blueprint.add_url_rule("book/update_book", "update_book", update_book, methods=["PUT", "POST"])
book_blueprint.add_url_rule("book/book_by_id", "book_by_id", book_by_id, methods=["GET"])
book_blueprint.add_url_rule("book/book_by_name", "book_by_name", book_by_name, methods=["GET"])
book_blueprint.add_url_rule("book/get_all_books", "get_all_books", get_all_books, methods=["GET"])