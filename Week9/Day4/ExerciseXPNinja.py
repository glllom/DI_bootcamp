class Creature:
    obj = 0

    @classmethod
    def instances_counter(cls):
        cls.obj += 1

    def __init__(self, weight, ate_food):
        self.next = ate_food
        self.id = self.obj
        self.instances_counter()
        self.locked = weight

    def find_nearest_food(self, grid):



class World:
    def __init__(self, grid):
        self.grid = grid
