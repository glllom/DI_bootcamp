class Human:
    def __init__(self, name, age, living_place=None):
        self.name = name
        self.age = age
        self.living_place = living_place

    def move(self, building):
        self.living_place = building
        building.inhabitants.append(self)


class Building:
    def __init__(self, address, inhabitants=None):
        if inhabitants is None:
            inhabitants = []
        self.address = address
        self.inhabitants = inhabitants

    def get_middle_age_of_inhabitants(self):
        return round(sum(map(lambda human: human.age, self.inhabitants)) / len(self.inhabitants), 1)


class City:
    def __init__(self, name, buildings=None):
        if buildings is None:
            buildings = []
        self.name = name
        self.buildings = buildings

    def construct(self, address):
        self.buildings.append(Building(address))

    def info(self, address):
        building = self.find_building(address)
        print(f"{len(building.inhabitants)} citizens live in the house at {address}. "
              f"Average age of citizens: {building.get_middle_age_of_inhabitants()}")

    def find_building(self, address):
        for building in self.buildings:
            if building.address == address:
                return building


tel_aviv = City('Tel Aviv')
tel_aviv.construct('Bialik 10')
john = Human('John Doe', 36)
mary = Human('Mary Doe', 30)
nikkie = Human('Nick Doe', 11)
john.move(tel_aviv.buildings[0])
mary.move(tel_aviv.buildings[0])
nikkie.move(tel_aviv.buildings[0])

tel_aviv.info('Bialik 10')


