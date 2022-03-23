from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField


class SearchInfo(FlaskForm):
    search_type = RadioField(choices=['Search by Name', 'Search by Phone'])
    name = StringField("Name: ")
    phone_number = StringField("Phone: ")
    submit = SubmitField()


