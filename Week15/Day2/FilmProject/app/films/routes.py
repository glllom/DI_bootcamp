from flask import Flask, render_template
from app.films import films_app


@films_app.route('/')
def hello_world():
    return render_template('homepage.html')


