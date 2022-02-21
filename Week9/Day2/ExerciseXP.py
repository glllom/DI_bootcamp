"""
Exercise 1 : Built-In Functions
"""
number = -15.5
print(number.__dir__())
print(number.__abs__())
print(number.__int__())


# word = input()

class Sample:
    """This is sample documentation for object"""
    pass


x = Sample
print(x.__doc__)


"""
Exercise 2: Currencies
"""


class Currency:
    def __init__(self, label, value):
        self.label = label
        self.value = value

    def __str__(self):
        return f'{self.value} {self.label}{"s" if self.value > 1 else ""}'

    def __repr__(self):
        return f'{self.value} {self.label}{"s" if self.value > 1 else ""}'

    def __int__(self):
        return self.value

    def __add__(self, other):
        if type(other) in (int, float):
            return Currency(self.label, self.value + other)
        elif isinstance(other, Currency) and self.label == other.label:
            return Currency(self.label, self.value + other.value)
        else:
            raise TypeError(f"Cannot add between Currency type {self.label} and {other.label}")

    def __iadd__(self, other):
        if type(other) in (int, float):
            return Currency(self.label, self.value + other)
        elif isinstance(other, Currency) and self.label == other.label:
            return Currency(self.label, self.value + other.value)
        else:
            raise TypeError(f"Cannot add between Currency type {self.label} and {other.label}")


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
print(int(c1))
print(repr(c1))
print(c1 + 5)
print(c1 + c2)
print("c1=", c1)
c1 += 5
print("c1=", c1)
c1 += c2
print("c1=", c1)
print(c1 + c3)