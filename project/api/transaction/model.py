from datetime import datetime

from project.extensions import db
from project.lib.model_utils import ResourceMixin, generate_uuid

class transaction(ResourceMixin, db.Model):
    __tablename__ = "transactions"

    transaction_id = db.Column(db.String(120), unique=True, nullable=False, primary_key=True, index=True, default=generate_uuid)
    user_id = db.Column(db.String(120), db.ForeignKey("users.user_id"))
    book_id = db.Column(db.String(120), db.ForeignKey("books.book_id"))
    issue_date = db.Column(db.DateTime)
    return_date = db.Column(db.DateTime)

# transaction = db.Table("transactions",
#                 db.Column("transaction_id", db.String(120), unique=True, nullable=False, primary_key=True, index=True, default=generate_uuid),
#                 db.Column("user_id", db.String(120), db.ForeignKey("users.user_id"), primary_key=True),
#                 db.Column("book_id", db.String(120), db.ForeignKey("books.book_id"), primary_key=True),
#                 db.Column("issue_date", db.DateTime),
#                 db.Column("return_date", db.DateTime)
# )