from constants import VALID_CMDS
from marshmallow import Schema, fields, validates_schema
from marshmallow.exceptions import ValidationError


class RequestParams(Schema):
    cmd1 = fields.String(required=True)
    cmd2 = fields.String(required=True)
    value1 = fields.String(required=True)
    value2 = fields.String(required=True)
    file = fields.String(required=True)

    @validates_schema
    def validate_cmd_params(self, values, **kwargs):
        if values['cmd1'] not in VALID_CMDS:
            raise ValidationError('"cmd1" contains invalid value')

        if values['cmd2'] not in VALID_CMDS:
            raise ValidationError('"cmd2" contains invalid value')
