"""
Exercise 1 : Pets
"""
class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Persian(Cat):
    def sing(self, sounds):
        return f'{sounds}'


jumbo = Persian('Jumbo', 2)
lola = Bengal('Lola', 1)
hunger = Chartreux('Hunger', 3)

my_cats = [jumbo, lola, hunger]

my_pets = Pets(my_cats)

print(*(my_pets.animals[i].walk() for i in range(len(my_pets.animals))), sep='\n')


"""
Exercise 2 : Dogs
"""
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        if self.weight * self.run_speed() > other_dog.weight * other_dog.run_speed():
            return f"{self.name} won the fight."
        else:
            return f"{other_dog.name} won the fight."


snoopy = Dog("Snoopy", 3, 10)
pluto = Dog("Pluto", 4, 20)
goofy = Dog("Goofy", 4, 25)

print(pluto.fight(goofy))



