import datetime
import math
import random

import faker

"""
Create a function that displays the current date.
Hint : Use the datetime module.
"""


def print_today():
    print(datetime.datetime.today().date())


"""
Exercise 2
Create a function that displays the amount of time left
 from now until January 1st."""


def print_time_left(target_date="01/01/2023"):
    d = datetime.datetime.strptime(target_date, '%m/%d/%Y')
    print((d - datetime.datetime.today()).days)


"""
Exercise 3
Create a function that accepts a birthdate as an argument (in the format of your choice),
 then display a message stating how many minutes the user has been alive."""


def minutes_counter(birthdate='05/12/1982'):
    birthdate = datetime.datetime.strptime(birthdate, '%d/%m/%Y')
    minutes = math.floor((datetime.datetime.today() - birthdate).total_seconds() / 60)
    print(f"You live totally {minutes} minutes")


minutes_counter()

"""Exercise 4
Write a function that display today’s date.
The function should also display the amount of time left from now until the next upcoming holiday and print which holiday that is. (Example: the next holiday is in 30 days and 12:03:45 hours).
Hint: Start by hardcoding the datetime and name of the upcoming holiday."""
next_holiday = "03/08/2022"

print_time_left(next_holiday)
print("days left until International Women's Day")

"""


Exercise 6 : Faker Module
Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code."""

users = []


def add_user():
    lang = random.choice(['en', 'it', 'ru_RU', 'de_DE', 'es_ES'])
    fake = faker.Faker(lang)
    users.append({'name': fake.name(),
                  'address': fake.address(),
                  'language_code': lang})


for _ in range(5):
    add_user()


print(*users, sep='\n')