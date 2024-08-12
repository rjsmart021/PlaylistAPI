from Playlist import db


class Songs(db.Model):
    """
    Customer Relation Model.
    Attributes are:
    1. Songs_id: integer and primary key. It will have auto increment
    2. Songs_name: string of max length 100 and null is not allowed
    3. Artist: string of max length 100 and null is not allowed
    4. Genre: string of max length 10 and null is not allowed
    """
    Songs_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Songs_name = db.Column(db.String(100), nullable=False)
    Artist = db.Column(db.String(100), nullable=False)
    Genre = db.Column(db.String(20), nullable=False)


class Playlist(db.Model):
    """
        Playlist Relation Model.
        Attributes are:
        1. Playlist_id: integer and primary key. It will have auto increment
        2. Playlist_name: string of max length 100 and null is not allowed
        3. Playlist_price: float and null is not allowed
        4. stock_available: Integer and null is not allowed
        """
    Playlist_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Playlist_name = db.Column(db.String(100), nullable=False)
    Playlist_price = db.Column(db.Float, nullable=False)
    stock_available = db.Column(db.Integer, nullable=False)


class Orders(db.Model):
    """
    Order Relation.
    """
    order_id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, nullable=False)
    expected_date = db.Column(db.Date, nullable=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('Songs.Songs_id'), nullable=False)


class OrderItem(db.Model):
    """
    Order Item relation.
    It refers to order and Playlist table.
    It will have all the list of playlist for a particular order.
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id'), nullable=False)
    Playlist_id = db.Column(db.Integer, db.ForeignKey('Playlist.Playlist_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
