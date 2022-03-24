from app import db
from datetime import date


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(32), index=True, unique=True)
    gender = db.Column(db.String(8))
    breed = db.Column(db.String(16))
    date_of_birth = db.Column(db.Date, default=date.today())
    details = db.Column(db.Text)
    price = db.Column(db.Integer)
    image = db.Column(db.String)
