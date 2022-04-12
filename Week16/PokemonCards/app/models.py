from app import db
import os
import json
from app.auth.models import users_pokemons
dirname = os.path.dirname(__file__)


class Pokemon(db.Model):
    pokemon_id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column("name", db.String(16), unique=True)
    pokemon_type = db.Column("type", db.String(32))
    base_price = db.Column("base_price", db.Integer)
    is_active = db.Column("is_active", db.Integer, default=1)
    status = db.Column(db.String, default="")
    owner = db.relationship("User", secondary=users_pokemons, back_populates="pokemon")


def add_pokemons_to_db():
    with open(f"{dirname}/static/data/all_pokemons.json", 'r') as f:
        all_pokemons = json.load(f)
        all_records = []
        for pokemon in all_pokemons:
            new_record = Pokemon(
                pokemon_id=pokemon['id'],
                name=pokemon['name'],
                pokemon_type=", ".join(pokemon['type']),
                base_price=pokemon['base_price']
            )
            all_records.append(new_record)
        return all_records


def sell_post(id):
    pokemon = Pokemon.query.get(id)
    pokemon.status = "for_sale"
    db.session.commit()


def buy_pokemon(id, current_user):
    bonus = 10  # for each part in transaction
    pokemon = Pokemon.query.get(id)
    old_owner = pokemon.owner
    if old_owner[0] == current_user:
        return "You can not buy your own Pokemon."
    pokemon.status = ""
    if old_owner:
        old_owner[0].money += pokemon.base_price + bonus
        old_owner[0].pokemon.remove(pokemon)
    current_user.pokemon.append(pokemon)
    current_user.money -= pokemon.base_price + bonus
    db.session.commit()
    return "Transaction approved."


def get_all_trades():
    return Pokemon.query.filter_by(status="for_sale")
