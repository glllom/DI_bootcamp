from app.films import db
from datetime import date

films_countries = db.Table('films_countries',
                           db.Column('country_id', db.Integer, db.ForeignKey('country.country_id')),
                           db.Column('film_id', db.Integer, db.ForeignKey('film.film_id'))
                           )

films_category = db.Table('films_category',
                          db.Column('category_id', db.Integer, db.ForeignKey('category.category_id')),
                          db.Column('film_id', db.Integer, db.ForeignKey('film.film_id'))
                          )


films_director = db.Table('films_director',
                          db.Column('director_id', db.Integer, db.ForeignKey('director.director_id')),
                          db.Column('film_id', db.Integer, db.ForeignKey('film.film_id'))
                          )


class Country(db.Model):
    country_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column("Name", db.String)
    films = db.relationship("Films", backref="country", lazy="dynamic")


class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String)


class Director(db.Model):
    director_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    first_name = db.Column("First Name", db.String)
    last_name = db.Column("Last Name", db.String)


class Film(db.Model):
    film_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    title = db.Column("Title", db.String)
    release_date = db.Column("Release Date", db.Date, default=date.today())
    created_in_country = db.Column(db.Integer, db.ForeignKey('country.country_id'))
    available_in_countries = db.relationship("Country", secondary=films_countries)
    category = db.relationship("Category", secondary=films_category)
    director = db.relationship("Director", secondary=films_director)
