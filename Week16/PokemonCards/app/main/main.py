from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from app import db
from app import models

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('auth/profile.html', name=current_user.name)


@main.route('/pok')
def show_pok():
    return render_template('pokemon_card.html')


@main.route('/load_all')
def load_all():
    for record in models.add_pokemons_to_db():
        db.session.add(record)
    db.session.commit()
    return redirect(url_for('main.index'))

