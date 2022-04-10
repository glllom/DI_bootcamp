from wtforms import SelectField, SubmitField
from flask_wtf import FlaskForm


class SelectCoin(FlaskForm):
    names = SelectField("Choose your coin:")
    submit = SubmitField()
