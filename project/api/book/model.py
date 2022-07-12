from project.extensions import db
from project.lib.model_utils import ResourceMixin, generate_uuid

class Book(ResourceMixin, db.Model):
    __tablename__ = "books"

    book_id = db.Column(db.String, unique=True, nullable=False, primary_key=True, index=True, default=generate_uuid)
    book_name = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    tag = db.Column(db.String(120))
    total_copies = db.Column(db.Integer, nullable=False)
    available_copies = db.Column(db.Integer, nullable=False)