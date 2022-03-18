"""
Exercise 1 : Temperature
"""


class Temperature:
    def __init__(self, temp):
        self.temp = temp


class Celsius(Temperature):
    def convert_to_fahrenheit(self):
        return Fahrenheit(self.temp * 9 / 5 + 32)

    def convert_to_kelvin(self):
        return Kelvin(self.temp - 273)


class Fahrenheit(Temperature):
    def convert_to_kelvin(self):
        return Kelvin((self.temp - 32) * 5 / 9 +273)

    def convert_to_celsius(self):
        return Celsius((self.temp - 32) * 5 / 9)


class Kelvin(Temperature):
    def convert_to_fahrenheit(self):
        return Fahrenheit((self.temp - 273) * 9 / 5 + 32)

    def convert_to_celsius(self):
        return Celsius(self.temp + 273)
