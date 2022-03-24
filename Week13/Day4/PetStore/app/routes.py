from app import flask_app
from flask import render_template, redirect, url_for


@flask_app.route("/")
def index():
    return render_template('index.html')


@flask_app.route("/pets")
def all_pets():
    return render_template('pets.html')


@flask_app.route("/pet/<int:pet_id>")
def pet_info(pet_id):
    return render_template('pet.html')
