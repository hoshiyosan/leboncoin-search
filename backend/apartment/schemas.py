from marshmallow import Schema, fields

class SearchFilters(Schema):
    min_rooms=fields.Integer(missing=1)
    max_rooms=fields.Integer(missing=10)
    min_price=fields.Integer(missing=0)
    max_price=fields.Integer(missing=1000000)
