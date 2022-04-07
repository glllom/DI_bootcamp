class Farm:
    def __init__(self, farm_name):
        self.farm_name = farm_name
        self.animals = {}

    def add_animal(self, animal, amount=1):
        if animal in self.animals:
            self.animals[animal] += amount
        else:
            self.animals[animal] = amount

    def get_info(self):
        strings = f"{self.farm_name}'s farm\n\n"
        for animal, amount in self.animals.items():
            strings += f"{animal} : {amount}\n"
        strings += "\n\tE-I-E-I-0!"
        return strings


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
