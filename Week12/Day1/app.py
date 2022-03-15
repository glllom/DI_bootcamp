from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length
from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)
app.secret_key = '13214465469847635431'


class SignUpForm(FlaskForm):
    first_name = StringField("First Name: ",
                            validators=[InputRequired(message="Please, tell me you name."), Length(min=4, max=10, message="Incorrect length")])
    last_name = StringField("Last Name: ",
                           validators=[InputRequired(message="Please, tell me you last name."), Length(min=4, max=10)])
    age = StringField("Age: ",
                      validators=[InputRequired(message="Please, tell me you age."), Length(min=1, max=3)])
    submit = SubmitField()

person = []
@app.route('/', methods=['GET', 'POST'])
def index():
    form = SignUpForm()
    global person
    if form.validate_on_submit():
        person.extend((form.first_name.data, form.last_name.data, form.age.data))
        return redirect(url_for("index"))
    return render_template("index.html", form=form, person=person)


if __name__ == '__main__':
    app.run()