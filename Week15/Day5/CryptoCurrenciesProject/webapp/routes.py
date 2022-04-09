from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user

from webapp import cripto_app, models, db
from werkzeug.security import generate_password_hash, check_password_hash
import flask_login


@cripto_app.route('/')
def homepage():
    return render_template("index.html")


@cripto_app.route('/login')
def login():
    return render_template("login.html")


@cripto_app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = bool(request.form.get('remember'))
    user = models.Users.query.filter_by(email=email).first()
    if not user:
        flash("This user doesn't exist")
        return redirect(url_for('login'))
    elif not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('login'))
    login_user(user, remember=remember)
    return redirect(url_for('homepage'))


@cripto_app.route('/signup')
def signup():
    return render_template('signup.html')


@cripto_app.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    if user := models.Users.query.filter_by(email=email).first():
        print('Email address already exists')
        flash('Email address already exists')
        return redirect(url_for('signup'))

    new_user = models.Users(email=email,
                            username=name,
                            password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('homepage'))


@cripto_app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))
