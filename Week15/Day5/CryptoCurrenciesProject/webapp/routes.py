from flask import render_template, redirect, url_for
from webapp import cripto_app, models, db, login_manager
import flask_login


@cripto_app.route('/')
def homepage():
    return render_template("index.html")


@cripto_app.route('/login', methods=['GET', 'POST'])
def login():
    print(flask_login.current_user.is_authenticated)
    return redirect(url_for('homepage'))


