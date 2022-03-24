from app import db

phones_table = db.Table('phones_persons', db.Column('person_id', db.Integer, db.ForeignKey('person.id')),
                        db.Column('phone_id', db.Integer, db.ForeignKey('phone_number.id'))
                        )


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(32), index=True, unique=True)
    email = db.Column(db.String(64), unique=True)
    phonenumbers = db.relationship("PhoneNumber", secondary=phones_table, back_populates="person")
    address = db.Column(db.String(64))


class PhoneNumber(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    number = db.Column(db.String(16), index=True, unique=True)
    person = db.relationship("Person", secondary=phones_table, back_populates="phonenumbers", uselist=False)
