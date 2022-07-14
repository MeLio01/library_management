import os
from flask import redirect, Blueprint, request, jsonify

from .interface import User
from .service import get_user_by_id, issued_books_service, get_user_by_name
from .schema import user_profile_schema, user_id_schema, user_out_schema

from project.lib.errors import BadRequest, BaseError

user_blueprint = Blueprint("user", __name__)

def add_user():
    auth = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization header invalid", 400)
    data = user_profile_schema.load(request.json)
    user = User.add_user(data)
    response = user_out_schema.dump(user)
    return response, 200

def delete_user():
    auth: str = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization header invalid", 400)
    data = user_id_schema.load(request.json)
    delete = User.delete_user_by_id(data["user_id"])
    if delete == False:
        raise BadRequest("User id invalid", 400)
    return True

def update_user():
    auth: str = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization header invalid", 400)
    data = user_out_schema.load(request.json)
    user = User.update_user_by_id(data)
    if user == None:
        raise BadRequest("User id invalid", 400)
    response = jsonify(user_out_schema.dump(user))
    return response, 200

def user_by_id():
    auth: str = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization header invalid", 400)
    data = user_id_schema.load(request.json)
    user = get_user_by_id(data["user_id"])
    if user == None:
        raise BadRequest("User id invalid", 400)
    response = jsonify(user_out_schema.dump(user))
    return response, 200

def user_by_name():
    auth: str = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization header invalid", 400)
    data = user_profile_schema.load(request.json)
    user = get_user_by_name(data)
    if user == None:
        raise BadRequest("User Name invalid", 400)
    response = jsonify(user_out_schema.dump(user))
    return response, 200

def issued_books_by_user():
    auth: str = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization header invalid", 400)
    data = user_id_schema.load(request.json)
    books = issued_books_service(data["user_id"])
    if books == None:
        raise BadRequest("User id Invalid", 400)
    return {"books": books}, 200

def get_all_users():
    auth: str = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization header invalid", 400)
    users = User.get_all_users()
    return {"users": users}, 200

user_blueprint.add_url_rule("user/add_user", "add_user", add_user, methods=["POST"])
user_blueprint.add_url_rule("user/delete_user", "delete_user", delete_user, methods=['DELETE'])
user_blueprint.add_url_rule("user/update_user", "update_user", update_user, methods=["POST", "PUT"])
user_blueprint.add_url_rule("user/user_by_id", "user_by_id", user_by_id, methods=["GET"])
user_blueprint.add_url_rule("user/user_by_name", "user_by_name", user_by_name, methods=["GET"])
user_blueprint.add_url_rule("user/issued_books", "issued books by user", issued_books_by_user, methods=["GET"])
user_blueprint.add_url_rule("user/get_all_users", "get all users", get_all_users, methods=["GET"])