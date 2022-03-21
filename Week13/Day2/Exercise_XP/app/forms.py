from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired


class AddUser(FlaskForm):
    user_name = StringField("Name", validators=[InputRequired()])
    street = StringField("Street", validators=[InputRequired()])
    city = StringField("City", validators=[InputRequired()])
    zipcode = StringField("Zipcode", validators=[InputRequired()])
    submit = SubmitField()
