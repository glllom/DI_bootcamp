import forms
from flask import Flask, redirect, render_template, url_for
app = Flask(__name__)
app.secret_key = '13214465469847635431'
person = {}


@app.route('/', methods=['GET', 'POST'])
def maim_form():
    form = forms.CvForm()
    if form.validate_on_submit():
        person['firstname'] = form.first_name.data
        person['lastname'] = form.last_name.data
        person['address'] = form.address.data
        person['phone'] = form.phone.data
        person['email'] = form.email.data
        person['summary'] = form.summary.data
        person['skills'] = form.skills.data
        person['education'] = form.education.data
        person['experience'] = form.experience.data
        person['certifications'] = form.certification.data
        person['languages'] = form.languages.data
        if form.template.data == 'Template 1':
            return redirect(url_for('template_1'))
        elif form.template.data == 'Template 2':
            return redirect(url_for('template_2'))
    return render_template("form.html", form=form)


@app.route('/template-1')
def template_1():
    return render_template("cv_1.html", person=person)


@app.route('/template-2')
def template_2():
    return render_template("cv_2.html", person=person)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
