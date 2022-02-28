from random import randint, choices
import string


def func_ex_2(x):
    print("Success" if x == randint(1, 100) else "Wrong")


def func_ex_3(length=5):
    return ''.join(choices(string.ascii_letters, k=length))



