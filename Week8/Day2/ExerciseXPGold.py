from random import random
"""
Exercise 1 : Geometry
"""
import math


class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def definition(self):
        print("A circle is the set of all points in the plane that are a fixed distance (the radius) from a fixed "
              "point (the centre).")


"""
Exercise 2 : Custom List Class
"""

class MyList:
    def __init__(self, letters):
        self.letters = letters

    def reversed(self):
        return self.letters[::-1]

    def sorted(self):
        return sorted(self.letters)

    def new_random(self):
        return [random() for _ in range(len(self.letters))]


"""
Exercise 3 : Restaurant Menu Manager
"""
