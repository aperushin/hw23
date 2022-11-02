from marshmallow import Schema, fields


class RequestParams(Schema):
    cmd1 = fields.String(required=True)
    cmd2 = fields.String(required=True)
    value1 = fields.String(required=True)
    value2 = fields.String(required=True)
    file = fields.String(required=True)
