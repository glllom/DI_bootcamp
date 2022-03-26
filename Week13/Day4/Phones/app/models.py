from app import db

phones_table = db.Table('phones_persons', db.Column('person_id', db.Integer, db.ForeignKey('person.id')),
                        db.Column('phone_id', db.Integer, db.ForeignKey('phone_number.id'))
                        )


nationality_table = db.Table('nationality_persons', db.Column('person_id', db.Integer, db.ForeignKey('person.id')),
                        db.Column('nationality_id', db.Integer, db.ForeignKey('nationality.nationality_id'))
                        )


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(32), index=True, unique=True)
    email = db.Column(db.String(64), unique=True)
    phonenumbers = db.relationship("PhoneNumber", secondary=phones_table, back_populates="person")
    address = db.Column(db.String(64))
    nationalities = db.relationship("Nationality", secondary=nationality_table, back_populates="people")


class PhoneNumber(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    number = db.Column(db.String(16), index=True, unique=True)
    person = db.relationship("Person", secondary=phones_table, back_populates="phonenumbers", uselist=False)


class Nationality(db.Model):
    nationality_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(16), index=True, unique=True)
    people = db.relationship("Person", secondary=nationality_table, back_populates="nationalities", uselist=False)
