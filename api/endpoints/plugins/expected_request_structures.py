"""
This file defines the expected structure of incoming request payloads so that they may used in endpoints.
"""
from marshmallow import Schema, fields, ValidationError, validates


#  The schema for the sort fields.
class SortOptionSchema(Schema):

    #  The column name to order by.
    by = fields.String(dump_only=True, required=True)
    #  The type of ordering.
    order = fields.String(dump_only=True, required=True)


#  Schema for GET plugins options
class PluginOptionsSchema(Schema):

    #  An optional count limiter for the number of items returned.
    count = fields.Integer(dump_only=True, required=False)
    #  An optional author id to filter by.
    author_id = fields.String(dump_only=True, required=False)
    #  A substring used in searching for matching titles.
    title_contains = fields.String(dump_only=True, required=False)
    #  A list of tag names to filter by.
    tags = fields.List(fields.String(), dump_only=True, required=False)
    #  A sorting object which contains two values: by, and order.
    sort = fields.Nested(SortOptionSchema, dump_only=True, required=False)

    @validates('count')
    def validate_count(self, count):
        if count < 1:
            raise ValidationError('Count must not be less than 1.')
