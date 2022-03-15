from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField, BooleanField
from wtforms.validators import InputRequired, NumberRange


class AddCity(FlaskForm):
    city = StringField("Name of the city:", validators=[InputRequired(message="This field is required.")])
    country = StringField("Name of the country:", validators=[InputRequired(message="This field is required.")])
    inhabitants = DecimalField("Amount of inhabitants:", validators=[InputRequired(message="This field is required."),
                                                                     NumberRange(min=1,
                                                                                 message="Number must be positive")])
    city_area = DecimalField("City's area (in square km):")
    latitude = StringField("Latitude:")
    longitude = StringField("Longitude:")
    capital = BooleanField("Capital")
    submit = SubmitField()
