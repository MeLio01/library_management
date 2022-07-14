import os
from flask import redirect, Blueprint, request, jsonify

from .interface import transaction
from .schema import issue_schema, transaction_id_schema, transaction_out_schema

from project.lib.errors import BadRequest, BaseError

trans_blueprint = Blueprint("transaction", __name__)

def issue_book():
    auth: str = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization header invalid", 400)
    data = issue_schema.load(request.json)
    trans = transaction.issue_book(data)
    response = transaction_out_schema.dump(trans)
    return response, 200

def return_book():
    auth: str = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization header invalid", 400)
    data = transaction_id_schema.load(request.json)
    trans = transaction.return_book(data)
    if trans == None:
        raise BadRequest("Transaction id invalid", 400)
    response = transaction_out_schema.dump(trans)
    return response, 200

def transaction_by_id():
    auth: str = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization header invalid", 400)
    data = transaction_id_schema.load(request.json)
    trans = transaction.get_transaction_by_id(data["transaction_id"])
    if trans == None:
        raise BadRequest("Transaction id invalid", 400)
    response = transaction_out_schema.dump(trans)
    return response, 200

def transaction_by_info():
    auth: str = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization header invalid")
    data = issue_schema.load(request.json)
    trans = transaction.get_transaction_by_info(data)
    if trans == None:
        raise BadRequest("Transaction info invalid", 400)
    response = transaction_out_schema.dump(trans)
    return response, 200

def delete_trasaction():
    auth: str = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization header invalid", 400)
    data = transaction_id_schema.load(request.json)
    trans = transaction.delete_transaction_by_id(data["transaction_id"])
    if trans == False:
        raise BadRequest("Transaction id invalid", 400)
    return True, 200


trans_blueprint.add_url_rule("trans/issue_book", "issue_book", issue_book, methods=["POST"])
trans_blueprint.add_url_rule("trans/return_book", "return_book", return_book, methods=["PUT", "POST"])
trans_blueprint.add_url_rule("trans/trans_by_id", "transaction_by_id", transaction_by_id, methods=["GET"])
trans_blueprint.add_url_rule("trans/trans_by_info", "transaction_by_info", transaction_by_info, methods=["GET"])
trans_blueprint.add_url_rule("trans/delete_trans", "delete_transaction", delete_trasaction, methods=["DELETE"])


