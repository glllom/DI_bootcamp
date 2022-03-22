import json
from app import flask_app
from app import db
from app.models import Users
from flask import render_template, redirect, url_for, flash
from forms import AddUser, DeleteUser, Login
import re
from random import choice


@flask_app.route("/")
@flask_app.route("/1")
@flask_app.route("/1<logged_user>")
def show_table_1(logged_user=None):
    caption = "1. Display all the users (with all the details)."
    if logged_user:
        logged_user = (logged_user, Users.query.filter_by(name=logged_user).first().status)
        if logged_user[1] == 'admin':
            print("logged as admin")
            users = Users.query.all()
        else:
            print("logged as client")
            users = Users.query.filter_by(status="client")
    else:
        users = Users.query.filter_by(status="client")
    return render_template('index.html', users=users, caption=caption, logged_user=logged_user)


@flask_app.route("/2")
def show_table_2():
    caption = "2. Only display the user(s) who live(s) in “Roscoeview”."
    users = Users.query.filter_by(city="Roscoeview")
    return render_template('index.html', users=users, caption=caption)


@flask_app.route("/3")
def show_table_3():
    caption = "3. Only display the first 5 users."
    users = Users.query.limit(5).all()
    return render_template('index.html', users=users, caption=caption)


@flask_app.route("/4")
def show_table_4():
    caption = "4. Only display the user(s) which zipcode starts with the number 5."
    users = Users.query.filter(Users.zipcode.startswith('5'))
    return render_template('index.html', users=users, caption=caption)


@flask_app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    form = AddUser()
    if form.validate_on_submit():
        new_user = Users(name=form.user_name.data,
                         street=form.street.data,
                         city=form.city.data,
                         zipcode=form.zipcode.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("show_table_1"))
    return render_template('add_user.html', form=form)


@flask_app.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    caption = "All the users."
    users = Users.query.all()
    form = DeleteUser()
    if form.validate_on_submit():
        user_to_delete = Users.query.filter_by(name=form.user_name.data).first()
        db.session.delete(user_to_delete)
        db.session.commit()
        return redirect(url_for("delete_user"))
    return render_template('delete_user.html', users=users, caption=caption, form=form)


@flask_app.route('/login', methods=['GET', 'POST'])
def login_user():
    form = Login()
    if form.validate_on_submit():
        name = form.name.data
        city = form.city.data
        users = Users.query.all()
        if not is_correct(name) or not is_correct(city):
            flash(f"{name} is not correct input.")
        elif (name, city) in list(map(lambda user: (user.name, user.city), users)):
            flash(f"You logged in as {name}.")
            return redirect(url_for("show_table_1", logged_user=name))
        else:
            flash(f"'{name}' doesn't exist or city is wrong. You need do sign up.")
            return redirect(url_for("add_user"))
    return render_template('login.html', form=form)


def populate():
    with open('users.json', 'r') as f:
        users = json.load(f)
    for user in users:
        new_user = Users(name=user['name'],
                         street=user['address']['street'],
                         city=user['address']['city'],
                         zipcode=user['address']['zipcode'])
        db.session.add(new_user)
        db.session.commit()


def is_correct(word):
    """
    Checks if there are only letters, digits or space in word
    """
    return bool(re.fullmatch(r'[\w ]+', word))


def appoint_status():
    for user in Users.query.all():
        user.status = choice(['admin', 'client'])
    db.update(Users)
    db.session.commit()

