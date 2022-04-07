import math


class Circle:
    """Circle can be defined by either specifying the radius(r) or the diameter(d)"""
    def __init__(self, **kwargs):
        if len(kwargs) > 1:
            raise ValueError("Argument can be only one ('r', or 'd')")
        if list(kwargs.keys())[0] == 'r':
            self.diam = kwargs['r'] * 2
        elif list(kwargs.keys())[0] == 'd':
            self.diam = kwargs['d']
        else:
            raise ValueError("Argument gan be either 'r', or 'd'")

    def get_diameter(self):
        return self.diam

    def get_radius(self):
        return self.diam / 2

    def get_area(self):
        return round(math.pi * (self.diam / 2) ** 2, 2)

    def print_circle(self):
        print(f"Circle with diameter {self.diam} and area {self.get_area()}.")

    def __add__(self, other):
        if isinstance(other, Circle):
            new_diam = pow((self.get_area() + other.get_area()) / math.pi, 0.5) * 2
            return Circle(d=new_diam)
        raise ValueError('Value Invalid')

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.diam > other.diam
        raise ValueError('Value Invalid')

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.diam == other.diam
        raise ValueError('Value Invalid')

    def __next__(self):
        return self


c1 = Circle(r=10)
c2 = Circle(d=10)
c3 = c1 + c2
c1.print_circle()
c2.print_circle()
c3.print_circle()

print(c1 == c2)
print(c1 > c2)

circle_list = [c1, c2, c3, Circle(r=1)]


for circle in circle_list:
    circle.print_circle()
print('*' * 30)
for circle in sorted(circle_list):
    circle.print_circle()
