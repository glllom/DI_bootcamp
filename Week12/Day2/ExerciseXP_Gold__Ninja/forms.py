from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import InputRequired


class AddCity(FlaskForm):
    city = StringField("Name of the city:", validators=[InputRequired(message="This field is required.")])
    country = StringField("Name of the country:", validators=[InputRequired(message="This field is required.")])
    inhabitants = DecimalField("Amount of inhabitants:", validators=[InputRequired(message="This field is required.")])
    city_area = DecimalField("City's area (in square km):")
    submit = SubmitField()