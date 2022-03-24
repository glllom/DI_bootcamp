from app.models import Pet
from app import db
import requests
#  2
new_pet = Pet(name='Jaw',
              gender='M',
              breed='dingo',
              details='A wild one!',
              price=5,
              image=(requests.get("https://dog.ceo/api/breed/dingo/images/random")).json()['message']
              )
db.session.add(new_pet)


#  3
new_pet = Pet(name='Sweety',
              gender='F',
              breed='chihuahua',
              details='Small and pretty.',
              price=700,
              image=(requests.get("https://dog.ceo/api/breed/chihuahua/images/random")).json()['message']
              )
db.session.add(new_pet)


#  4
new_pet = Pet(name='Nanny',
              gender='F',
              breed='golden retriever',
              details='Where is a baby? I am the best nanny!',
              price=300,
              image=(requests.get("https://dog.ceo/api/breed/retriever/golden/images/random")).json()['message']
              )
db.session.add(new_pet)


#  5
new_pet = Pet(name='Pathfinder',
              gender='M',
              breed='border collie',
              details='Sheep are so stupid.',
              price=1000,
              image=(requests.get("https://dog.ceo/api/breed/collie/border/images/random")).json()['message']
              )
db.session.add(new_pet)


#  6
new_pet = Pet(name='mr.Captain',
              gender='M',
              breed='doberman',
              details='I serve the people!',
              price=515,
              image=(requests.get("https://dog.ceo/api/breed/doberman/images/random")).json()['message']
              )
db.session.add(new_pet)







db.session.commit()
