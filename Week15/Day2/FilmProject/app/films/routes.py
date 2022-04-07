from flask import render_template, redirect, url_for
from app.films import films_app
from app.films.forms import AddFilmForm, AddDirectorForm, AddCategoryForm, AddCountryForm
from app.films import models, db


@films_app.route('/')
def homepage():
    films = models.Film.query.all()
    return render_template('homepage.html', films=films)


@films_app.route('/addFilm', methods=["get", "post"])
def add_film():
    form = AddFilmForm()
    choices_countries = [
        (record.country_id, record.name) for record in models.Country.query.all()
    ]
    choices_directors = [
        (record.director_id, f"{record.first_name} {record.last_name}") for record in models.Director.query.all()
    ]
    choices_categories = [
        (record.category_id, record.name) for record in models.Category.query.all()
    ]
    form.created_in_country.choices = choices_countries
    form.director.choices = choices_directors
    form.category.choices = choices_categories
    form.available_in_countries.choices = choices_countries
    if form.is_submitted():  # WHY???
        available_countries = [
            models.Country.query.get(country)
            for country in form.available_in_countries.data
        ]
        directors = [
            models.Director.query.get(country)
            for country in form.director.data
        ]
        category = [
            models.Category.query.get(country)
            for country in form.category.data
        ]
        new_film = models.Film(title=form.title.data,
                               release_date=form.release_date.data,
                               created_in_country=form.created_in_country.data,
                               available_in_countries=available_countries,
                               director=directors, category=category)
        db.session.add(new_film)
        db.session.commit()
        return redirect(url_for("homepage"))
    return render_template("film/addFilm.html", form=form)


@films_app.route('/addDirector', methods=["get", "post"])
def add_director():
    form = AddDirectorForm()
    if form.validate_on_submit():
        new_director = models.Director(first_name=form.first_name.data,
                                       last_name=form.last_name.data)
        db.session.add(new_director)
        db.session.commit()
        return redirect(url_for("homepage"))
    return render_template("director/addDirector.html", form=form)


@films_app.route('/addCategory', methods=["get", "post"])
def add_category():
    form = AddCategoryForm()
    if form.validate_on_submit():
        new_category = models.Category(name=form.name.data)
        db.session.add(new_category)
        db.session.commit()
        return redirect(url_for("homepage"))
    return render_template("film/addCategory.html", form=form)


@films_app.route('/addCountry', methods=["get", "post"])
def add_country():
    form = AddCountryForm()
    if form.validate_on_submit():
        new_country = models.Country(name=form.name.data)
        db.session.add(new_country)
        db.session.commit()
        return redirect(url_for("homepage"))
    return render_template("film/addCategory.html", form=form)


@films_app.route('/modifyFilm/<int:film_id>', methods=["get", "post"])
def modify_film(film_id):
    form = AddFilmForm()
    film = models.Film.query.get(film_id)
    choices_countries = [
        (record.country_id, record.name) for record in models.Country.query.all()
    ]
    choices_directors = [
        (record.director_id, f"{record.first_name} {record.last_name}") for record in models.Director.query.all()
    ]
    choices_categories = [
        (record.category_id, record.name) for record in models.Category.query.all()
    ]
    form.created_in_country.choices = choices_countries
    form.director.choices = choices_directors
    form.category.choices = choices_categories
    form.available_in_countries.choices = choices_countries
    form.title.data = film.title
    form.release_date.data = film.release_date
    form.created_in_country.data = film.created_in_country
    form.created_in_country.data = film.created_in_country

    if form.is_submitted():  # WHY???
        available_countries = [
            models.Country.query.get(country)
            for country in form.available_in_countries.data
        ]
        directors = [
            models.Director.query.get(country)
            for country in form.director.data
        ]
        category = [
            models.Category.query.get(country)
            for country in form.category.data
        ]
        film.update(title=form.title.data,
                    release_date=form.release_date.data,
                    created_in_country=form.created_in_country.data,
                    available_in_countries=available_countries,
                    director=directors, category=category)
        db.session.commit()
        return redirect(url_for("homepage"))
    return render_template("film/addFilm.html", form=form)
