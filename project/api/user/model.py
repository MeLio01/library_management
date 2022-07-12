from project.extensions import db
from project.lib.model_utils import ResourceMixin, generate_uuid
from project.api.transaction import transaction

class User(ResourceMixin, db.Model):
    __tablename__ = 'users'
    
    user_id = db.Column(db.String(120), unique=True, nullable=False, primary_key=True, index=True, default=generate_uuid)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120))
    phone_no = db.Column(db.String(12))
    email_id = db.Column(db.String(120), unique=True, nullable=False)