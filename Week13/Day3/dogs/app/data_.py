from app.models import Dog, Human
from app import db


my_human = Human(name="John")
my_dog = Dog(name="Rex", race="Chinchilla", human=my_human)

db.session.add(my_human)
db.session.add(my_dog)
db.session.commit()