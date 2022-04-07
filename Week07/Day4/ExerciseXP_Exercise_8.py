"""
Exercise 8
"""


def exercise_8(digit):
    print(sum(int(str(digit)*i) for i in range(1, 5)))


exercise_8(input("Give me a number from 1 to 9: "))
