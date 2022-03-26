from faker import Faker
from faker.providers import phone_number, address
from random import choices
from app.models import Person, PhoneNumber, Nationality
from app import db


def collect_names(amount=1):
    for _ in range(amount):
        fake = Faker()
        fake.add_provider(address)
        amount_phone_numbers = choices([1, 2, 3], weights=[5, 4, 1], k=1)[0]

        new_person = Person(name=fake.name(),
                            address=fake.address(),
                            email=fake.email())
        db.session.add(new_person)
        for _ in range(amount_phone_numbers):
            fake.add_provider(phone_number)
            new_phone = PhoneNumber(number=fake.phone_number(), person=new_person)
            db.session.add(new_phone)
    db.session.commit()
    db.create_all()


def add_nations():
    nationalities = Nationality.query.all()
    persons = Person.query.all()
    for person in persons:
        for nationality in choices(nationalities, k=2):
            person.nationalities = nationality
#  collect_names(50)
#  add_nations()
