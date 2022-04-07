from webapp import db


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    username = db.Column("username", db.String(32), unique=True, nullable=False)
    email = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(32), nullable=False)
