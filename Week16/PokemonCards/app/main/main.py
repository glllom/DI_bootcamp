from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app import models

main = Blueprint('main', __name__)


@main.route('/')
def index():
    all_trades = models.get_all_trades()
    return render_template('index.html', pokemons_list=all_trades)


@main.route('/profile')
@login_required
def profile():
    return render_template('auth/profile.html')


@main.route('/post_sell/<int:pokemon_id>')
@login_required
def post_sell(pokemon_id):
    models.sell_post(pokemon_id)
    return redirect(url_for('main.profile'))


@main.route('/buy_pokemon/<int:pokemon_id>')
@login_required
def buy_pokemon(pokemon_id):
    flash(models.buy_pokemon(pokemon_id, current_user))
    return redirect(url_for('main.index'))


@main.route('/load_all')
def load_all():
    for record in models.add_pokemons_to_db():
        db.session.add(record)
    db.session.commit()
    return redirect(url_for('main.index'))

