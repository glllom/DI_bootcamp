from app import db
import os
import json
dirname = os.path.dirname(__file__)


class Pokemon(db.Model):
    pokemon_id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column("name", db.String(16), unique=True)
    pokemon_type = db.Column("type", db.String(32))
    base_price = db.Column("base_price", db.Integer)
    is_active = db.Column("is_active", db.Integer, default=1)


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
