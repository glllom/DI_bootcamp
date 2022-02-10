import random

"""
Exercise 1
"""


def display_message():
    print("Hello, World. I learn Python.")


display_message()

"""
Exercise 2: 
"""


def favorite_book(title):
    print(f"One of my favorite books is {title}.")


favorite_book("The Witcher")

"""
Exercise 3 : Some Geography
"""


def describe_city(name_of_city, country="Israel"):
    print(f"{name_of_city} is in {country}.")


describe_city("Tel-Aviv")
describe_city("Los Angeles", "USA")

"""
Exercise 4 : Random
"""


def guess_number(number):
    x = random.randint(1, 100)
    if number == x:
        print("Success! You guessed a number")
    else:
        print(f"Fail! Your number is {number} and mine is {x}")


#  guess_number(int(input("Input the number: "))) <-- uncomment it!

"""
Exercise 5
"""


def make_shirt(size="L", message="I love Python"):
    print(f'Your shirt has size {size} and message "{message}".')


make_shirt("L")
make_shirt("M")
make_shirt("XXS", "Tiny")


def make_shirt2(*args):
    print(f'Your shirt has size {args[0]} and message "{args[1]}".')


make_shirt2("XXXXXL", "I am Hulk")


def make_shirt3(**kwargs):
    print(f'Your shirt has size {kwargs["size"]} and message "{kwargs["message"]}".')


make_shirt3(size="M", message="Just awesome!")

"""
Exercise 6
"""
magicians = ["Gandalf", "Saruman", "Merlin"]


def show_magicians(magicians_list):
    print(*magicians_list, sep=", ")


def make_great(magician_list):
    for i in range(len(magician_list)):
        magician_list[i] = "the Great " + magician_list[i]


show_magicians(magicians)
make_great(magicians)
show_magicians(magicians)
