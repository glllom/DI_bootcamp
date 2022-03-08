import random
from threading import Lock
import copy


class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances or args or kwargs:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class GameOfLife(metaclass=SingletonMeta):
    def __init__(self, width=20, height=20):
        self.__width = width
        self.__height = height
        self.world = self.generate_universe()
        self.counter_of_generations = 0
        self.old_world = self.world
        self.ages = self.world
        self.growing_age = 3
        self.adults = 0
        self.aging_age = 7
        self.olders = 0
        self.deaths = 0
        self.children = self.children_counter()

    def aging(self):
        for i in range(len(self.ages)):
            for j in range(len(self.ages[0])):
                if self.world[i][j] == 1:
                    self.ages[i][j] += 1
                else:
                    self.ages[i][j] = 0

    def children_counter(self):
        counter = 0
        for i in range(len(self.ages)):
            for j in range(len(self.ages[0])):
                if 0 < self.ages[i][j] < self.growing_age:
                    counter += 1
        return counter

    def adults_counter(self):
        for i in range(len(self.ages)):
            for j in range(len(self.ages[0])):
                if self.growing_age <= self.ages[i][j] < self.aging_age:
                    self.adults += 1

    def olders_counter(self):
        for i in range(len(self.ages)):
            for j in range(len(self.ages[0])):
                if self.aging_age <= self.ages[i][j]:
                    self.olders += 1

    def deaths_counter(self):
        for i in range(len(self.ages)):
            for j in range(len(self.ages[0])):
                if self.world[i][j] == 0 and self.old_world[i][j] == 1:
                    self.deaths += 1

    def form_new_generation(self):
        self.children = 0
        self.adults = 0
        self.olders = 0
        self.deaths = 0
        universe = self.world
        self.old_world = copy.deepcopy(self.world)
        new_world = [[0 for _ in range(self.__width)] for _ in range(self.__height)]

        for i in range(len(universe)):
            for j in range(len(universe[0])):

                if universe[i][j]:
                    if self.__get_near(universe, [i, j]) not in (2, 3):
                        new_world[i][j] = 0
                        continue
                    new_world[i][j] = 1
                    continue

                if self.__get_near(universe, [i, j]) == 3:
                    new_world[i][j] = 1
                    continue
                new_world[i][j] = 0
        self.world = new_world
        self.aging()
        self.children = self.children_counter()
        self.adults_counter()
        self.olders_counter()
        self.deaths_counter()

    def generate_universe(self):
        return [[random.randint(0, 1) for _ in range(self.__width)] for _ in range(self.__height)]

    @staticmethod
    def __get_near(universe, pos, system=None):
        if system is None:
            system = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

        count = 0
        for i in system:
            if universe[(pos[0] + i[0]) % len(universe)][(pos[1] + i[1]) % len(universe[0])]:
                count += 1
        return count

