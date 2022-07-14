from marshmallow import Schema, fields

def validate_phone_no(number):
    pass

class UserProfileSchema(Schema):
    first_name = fields.String(required=True)
    last_name = fields.String()
    phone_no = fields.String(validate=validate_phone_no)
    email_id = fields.String()
    books = fields.List(fields.String())

class UserIdSchema(Schema):
    user_id = fields.String(required=True)

class UserOut(UserProfileSchema, UserIdSchema):
    pass

user_profile_schema = UserProfileSchema()
user_id_schema = UserIdSchema()
user_out_schema = UserOut()