from app import flask_app
from flask import render_template, redirect, url_for
from app.app_forms import SearchInfo
from app.models import Person, PhoneNumber


@flask_app.route("/", methods=['GET', 'POST'])
def index():
    form = SearchInfo()
    if form.validate_on_submit():
        name = form.name.data
        phone = form.phone_number.data
        radio = form.search_type.data
        if radio == "Search by Name" and name:
            return redirect(url_for("find_by_name", name=name))
        elif radio == "Search by Phone" and phone:
            return redirect(url_for("find_by_phone", phone_number=phone))
    return render_template('index.html', form=form)


@flask_app.route('/person/by_phone<phone_number>')
def find_by_phone(phone_number):
    try:
        person = PhoneNumber.query.filter_by(number=phone_number).first().person
    except AttributeError:
        person = None
    return render_template('person_info.html', person=person)


@flask_app.route('/person/by_name<name>')
def find_by_name(name):
    print(name)
    try:
        person = Person.query.filter_by(name=name).first()
    except AttributeError:
        person = None
    return render_template('person_info.html', person=person)
