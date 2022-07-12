from marshmallow import Schema, fields

class BookProfileSchema(Schema):
    book_name = fields.String(required=True)
    author = fields.String()
    tag = fields.String()
    total_copies = fields.String()
    available_copies = fields.String()

class BookIdSchema(Schema):
    book_id = fields.String(required=True)

class BookOutSchema(BookProfileSchema, BookIdSchema):
    pass

book_profile_schema = BookProfileSchema()
book_id_schema = BookIdSchema()
book_out_schema = BookOutSchema()