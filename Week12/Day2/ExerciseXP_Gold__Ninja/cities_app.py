import random
from forms import AddCity
from flask import Flask, redirect, render_template, url_for
app = Flask(__name__)
app.config['SECRET_KEY'] = ''.join([chr(random.randint(97, 122)) for _ in range(256)])
city = {}


@app.route('/', methods=['GET', 'POST'])
def homepage():
    form = AddCity()
    if form.validate_on_submit():
        city['city_name'] = form.city.data
        city['country'] = form.country.data
        city['inhabitants'] = form.inhabitants.data
        city['city_area'] = form.city_area.data
        return redirect(url_for('view'))
    return render_template('cities.html', form=form)


@app.route('/view')
def view():
    return render_template('view.html', city=city)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
