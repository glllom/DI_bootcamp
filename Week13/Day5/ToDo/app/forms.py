from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length


class AddToDo(FlaskForm):
    task = StringField('New Task: ', validators=[InputRequired(message='Please input a new task'),
                                                 Length(min=2, max=20)])
    url = StringField('URL: ', validators=[InputRequired(message='Please input a new task')])
    submit = SubmitField()
