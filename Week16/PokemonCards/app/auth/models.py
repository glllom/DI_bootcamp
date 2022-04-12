# sourcery skip: avoid-builtin-shadow
from flask_login import UserMixin
from app import db


users_pokemons = db.Table('users_pokemons',
                          db.Column('users_id', db.Integer, db.ForeignKey('user.id')),
                          db.Column('pokemon_id', db.Integer, db.ForeignKey('pokemon.pokemon_id'))
                          )


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    pokemon = db.relationship("Pokemon", secondary=users_pokemons, back_populates="owner")
    money = db.Column(db.Integer, default=300)
