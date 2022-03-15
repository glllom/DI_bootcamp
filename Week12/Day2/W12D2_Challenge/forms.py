from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, FileField, SubmitField, SelectField
from wtforms.validators import InputRequired, Length
from flask_wtf.file import FileAllowed
from wtforms.widgets import TextArea


class CvForm(FlaskForm):
    first_name = StringField("Your First Name: ", validators=[InputRequired(message="This field is required.")])
    last_name = StringField("Your Last Name: ", validators=[InputRequired(message="This field is required.")])
    # photo = FileField("Upload your photo here", validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    address = StringField("Your Address: ", validators=[InputRequired(message="This field is required.")])
    phone = StringField("Your Phone: ")
    email = EmailField("Your e-mail: ", validators=[InputRequired(message="This field is required.")])
    languages = StringField("Languages you speak: ")
    summary = StringField("Place your summary information here: ", widget=TextArea(),
                          validators=[Length(max=200, message="Maximum 200 "
                                                              "signs")])
    skills = StringField("Place your skill highlights here: ", widget=TextArea(),
                         validators=[Length(max=150, message="Maximum 150 "
                                                             "signs")])
    experience = StringField("What is your experience: ", widget=TextArea(),
                             validators=[Length(max=200, message="Maximum 200 "
                                                                 "signs")])
    education = StringField("Place your education info here: ", widget=TextArea(),
                            validators=[Length(max=150, message="Maximum 150 "
                                                                "signs")])
    certification = StringField("Place your certifications here: ", widget=TextArea(),
                                validators=[Length(max=150, message="Maximum 150 "
                                                                    "signs")])
    template = SelectField(choices=['Template 1', 'Template 2'], validators=[InputRequired()])
    submit = SubmitField()
