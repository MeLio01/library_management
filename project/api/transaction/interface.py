from dataclasses import dataclass
from typing import Dict, Any
from datetime import datetime

from project.extensions import db
from project.api.book import BookDB

from .model import transaction as transactionDB

@dataclass
class transaction:
    transaction_id: str
    user_id: str    
    book_id: str
    issue_date: str
    return_date: str

    @classmethod
    def instance_creator(cls, transaction_db: transactionDB):
        return cls(
            transaction_id = transaction_db.transaction_id,
            user_id = transaction_db.user_id,
            book_id = transaction_db.book_id,
            issue_date = transaction_db.issue_date,
            return_date = transaction_db.return_date
        )
    
    @classmethod
    def issue_book(cls, info: Dict[str, Any]):
        book_db: BookDB = BookDB.get_first({"book_id": info["book_id"]})
        if book_db:
            if book_db.available_copies > 0:
                trans_db = transactionDB(
                    user_id = info["user_id"],
                    book_id = info["book_id"],
                    issue_date = datetime.utcnow()
                )
                trans_db.create()
                if trans_db:
                    book_db.available_copies -= 1
                    db.session.commit()
                    return cls.instance_creator(trans_db)
            else: 
                return "Book Unavailable"
        return None

    @classmethod
    def return_book(cls, info: Dict[str, Any]):
        trans_db: transactionDB = transactionDB.get_first({"transaction_id": info["transaction_id"]})
        book_db: BookDB = BookDB.get_first({"book_id": trans_db.book_id})
        if trans_db:
            trans_db.return_date = datetime.utcnow()
            book_db.available_copies += 1
            db.session.commit()
            return cls.instance_creator(trans_db)
        return None
    
    @classmethod
    def get_transaction_by_id(cls, trans_id):
        trans_db: transactionDB = transactionDB.get_first({"transaction_id": trans_id})
        if trans_db:
            return cls.instance_creator(trans_db)
        return None
    
    @classmethod
    def get_transaction_by_info(cls, transinfo: Dict[str, Any]):
        trans_db: transactionDB = transactionDB.get_first({"user_id": transinfo["user_id"], "book_id": transinfo["book_id"]})
        if trans_db:
            return cls.instance_creator(trans_db)
        return None
    
    @classmethod
    def delete_transaction_by_id(cls, trans_id):
        trans_db: transactionDB = transactionDB.get_first({"transaction_id": trans_id})
        if trans_db:
            trans_db.delete()
            return True
        return False
        
