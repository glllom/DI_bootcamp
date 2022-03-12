from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField


class SearchForm(FlaskForm):
    search_type = RadioField()
    submit = SubmitField("Search")


