"""
Exercise 1: Cats
"""


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def find_oldest_cat(*args):
    return max(args, key=lambda cat: cat.age)


tom = Cat("Tom", 4)
simon = Cat("Simon", 3)
katie = Cat("Katie", 1)

oldest_cat = find_oldest_cat(tom, simon, katie)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")

"""
Exercise 2 : Dogs
"""


class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2}cm high!")


def biggest_dog(*args):
    return max(args, key=lambda dog: dog.height)


davids_dog = Dog("Rex", 50)
davids_dog.bark()
davids_dog.jump()
sarahs_dog = Dog("Teacup", 20)
sarahs_dog.bark()
sarahs_dog.jump()

print(f"The biggest dog is {biggest_dog(davids_dog, sarahs_dog).name}")

"""
Exercise 3 : Who’s The Song Producer?
"""


class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        print(*self.lyrics, sep='\n')


stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()


"""
Exercise 4 : Afternoon At The Zoo
"""
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(*self.animals, sep=', ')

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            raise ValueError(f"There is no any {animal_sold} in this zoo.")

    def sort_animals(self):
        groups = {}
        counter, first_letter = 0, ""

        for animal in sorted(self.animals):
            if animal[0].upper() != first_letter:
                counter += 1
                first_letter = animal[0].upper()
                groups[counter] = [animal]
            else:
                groups[counter].append(animal)
                groups[counter].sort()
        return groups

    def get_groups(self):
        print(self.sort_animals(), sep='\n')


ramat_gan_safari = Zoo("Ramat Gan Safari")
ramat_gan_safari.add_animal("Baboon")
ramat_gan_safari.add_animal("Cat")
ramat_gan_safari.add_animal("Emu")
ramat_gan_safari.add_animal("Eel")
ramat_gan_safari.add_animal("Cougar")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Ape")
ramat_gan_safari.add_animal("Giraffe")

ramat_gan_safari.get_animals()

ramat_gan_safari.get_groups()

ramat_gan_safari.sell_animal("Giraffe")

ramat_gan_safari.get_groups()

