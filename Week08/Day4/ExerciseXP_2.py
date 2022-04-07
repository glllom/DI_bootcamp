from random import randint
from ExerciseXP import Dog

"""
Exercise 3 : Dogs Domesticated
"""


class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *other_dogs):
        print(*([dog.name for dog in other_dogs]), sep=', ', end=' ')
        print(f"and {self.name} all play together.")

    def do_a_trick(self):
        tricks = [f"{self.name} does a barrel roll.",
                  f"{self.name} stands on his back legs.",
                  f"{self.name} shakes your hand.",
                  f"{self.name} plays dead."]
        print(tricks[randint(0, 3)])


dog1 = PetDog('dog1', 2, 10)
dog2 = PetDog('dog2', 2, 10)
dog3 = PetDog('dog3', 2, 10)
dog4 = PetDog('dog4', 2, 10)

dog3.train()

dog2.play(dog1, dog3, dog4)
dog4.do_a_trick()
dog4.do_a_trick()
dog4.do_a_trick()
dog4.do_a_trick()
