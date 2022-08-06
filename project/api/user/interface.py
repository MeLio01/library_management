from collections import UserString
from dataclasses import dataclass
from typing import Dict, Any

from project.extensions import db
from project.api.transaction import transactionDB

from .model import User as UserDB

@dataclass
class User:
    user_id: str
    first_name: str
    last_name: str
    phone_no: str
    email_id: str

    @classmethod
    def instance_creator(cls, user_db: UserDB):
        return cls(
            user_id=user_db.user_id,
            first_name=user_db.first_name,
            last_name=user_db.last_name,
            phone_no=user_db.phone_no,
            email_id=user_db.email_id,
        )
    
    @classmethod
    def get_user_by_id(cls, user_id):
        user = UserDB.get_first({"user_id": user_id})
        if user:
            return cls.instance_creator(user_db=user)
        return None
    
    @classmethod
    def get_user_by_name(cls, userinfo: Dict[str, Any]):
        user_db: UserDB = UserDB.get_first({"first_name": userinfo["first_name"]})
        if user_db:
            return cls.instance_creator(user_db=user_db)
        return None
    
    @classmethod
    def add_user(cls, userinfo: Dict[str, Any]):
        user_db = UserDB(
            first_name=userinfo["first_name"],
            last_name=userinfo["last_name"],
            phone_no=userinfo["phone_no"],
            email_id=userinfo["email_id"]
        )
        user_db.create()
        if user_db:
            return cls.instance_creator(user_db)
        return None

    @classmethod
    def delete_user_by_id(cls, user_id):
        user_db: UserDB = UserDB.get_first({"user_id": user_id})
        if user_db:
            user_db.delete()
            return True
        return False
    
    @classmethod
    def update_user_by_id(cls, userinfo: Dict[str, Any]):
        user_db: UserDB = UserDB.get_first({"user_id": userinfo["user_id"]})
        if user_db:
            user_db = user_db.update(**userinfo)
            return cls.instance_creator(user_db)
        return None
    
    @classmethod
    def get_issued_books_by_user(cls, user_id):
        trans_db: transactionDB = transactionDB.get_all({"user_id": user_id})
        if trans_db:
            return [trans.transaction_id for trans in trans_db]
        return None

    @classmethod
    def get_all_users(cls):
        users = UserDB.get_all()
        if users:
            return [cls.instance_creator(user_db) for user_db in users]
        return None