from app import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(32))
    street = db.Column(db.String(16))
    city = db.Column(db.String(16))
    zipcode = db.Column(db.String(16))
    status = db.Column(db.String(16))

