from app import flask_app
from flask import render_template, redirect, url_for
from app.models import Pet


@flask_app.route("/")
def index():
    return render_template('index.html')


@flask_app.route("/pets")
def all_pets():
    pets = Pet.query.all()
    return render_template('pets.html', pets=pets)


@flask_app.route("/pet/<int:pet_id>")
def pet_info(pet_id):
    pet = Pet.query.get(pet_id)
    return render_template('pet.html', pet=pet)
