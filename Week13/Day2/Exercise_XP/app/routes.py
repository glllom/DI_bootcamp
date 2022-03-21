import json
from app import flask_app
from app import db
from app.models import Users
from flask import render_template, redirect, url_for
from forms import AddUser


@flask_app.route("/")
@flask_app.route("/1")
def show_table_1():
    caption = "1. Display all the users (with all the details)."
    users = Users.query.all()
    return render_template('index.html', users=users, caption=caption)


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
                         zipcode=form.zipcode)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("show_table_1"))
    return render_template('add_user.html', form=form)


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




