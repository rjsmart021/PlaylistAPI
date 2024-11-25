from flask_marshmallow import Marshmallow
from marshmallow import fields, validate
from Playlist import app

ma = Marshmallow()

class CustomerSchema(ma.Schema):
    Songs_id = fields.Integer(dump_only=True)
    Songs_name = fields.String(required=True)
    Artist_Name = fields.Email(required=True, validate=validate.Regexp(r'^.+@[^\.].*\.[a-z]{2,}$',
                                                                 error='Invalid'))
    Genre = fields.String(required=True, validate=validate.Length(min=10, max=20,
                                                                         error='Invalid '))


class PlaylistSchema(ma.Schema):
    playlist_id = fields.Integer(required=True)
    playlist_name = fields.String(required=True)
    playlist_price = fields.Float(required=True)
    stock_available = fields.Integer(required=True)


class OrdersSchema(ma.Schema):
    order_id = fields.Integer(dump_only=True)
    order_date = fields.DateTime(required=True)
    expected_date = fields.Date(allow_none=True)
    Songs_id = fields.Integer(required=True)


class OrderItemSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    order_id = fields.Integer(required=True)
    playlist_id = fields.Integer(required=True)
    quantity = fields.Integer(required=True)
    price = fields.Float(required=True)


ma.init_app(app)
