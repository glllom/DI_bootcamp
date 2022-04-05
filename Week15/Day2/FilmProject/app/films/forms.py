from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SelectMultipleField, SubmitField
from wtforms.validators import InputRequired


class AddFilmForm(FlaskForm):
    title = StringField("Title", validators=[InputRequired()])
    release_date = DateField("Release Date", validators=[InputRequired()])
    created_in_country = SelectField("Country", validators=[InputRequired()])
    # available_in_countries = SelectMultipleField("Available in countries ", validators=[InputRequired()])
    category = SelectField("Category", validators=[InputRequired()])
    director = SelectField("Director", validators=[InputRequired()])
    submit = SubmitField()


class AddDirectorForm(FlaskForm):
    first_name = StringField("First Name", validators=[InputRequired()])
    last_name = StringField("Last Name", validators=[InputRequired()])
    submit = SubmitField()


class AddCategoryForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired()])
    submit = SubmitField()
