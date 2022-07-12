from marshmallow import Schema, fields

class IssueSchema(Schema):
    user_id = fields.String(required=True)
    book_id = fields.String(required=True)
    issue_date = fields.String()
    return_date = fields.String()

class TransactionIdSchema(Schema):
    transaction_id = fields.String(required=True)

class TransactionOutSchema(IssueSchema, TransactionIdSchema):
    pass

issue_schema = IssueSchema()
transaction_id_schema = TransactionIdSchema()
transaction_out_schema = TransactionOutSchema()