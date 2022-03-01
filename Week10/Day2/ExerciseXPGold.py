import re
from random import randint, choices, choice, sample


def return_numbers(expression):
    return ''.join(re.findall(r"\d", expression))


def validate_name(name="Michael Jackson"):
    return bool(re.fullmatch(r"[A-Z][a-z]+ [A-Z][a-z]+", name))


def password_generator():
    length_pass = 0
    password = ''
    while True:
        try:
            length_pass = int(input("Please enter the length of password (6-30 characters): "))
        except ValueError:
            print("Invalid number")
            continue
        if 30 < length_pass or length_pass < 6:
            print("Number must be between 6 and 30 characters.")
            continue
        break
    password += chr(randint(48, 57))  # digits
    password += chr(randint(65, 90))  # Capital letters
    password += chr(randint(97, 122))  # lowercase letters
    password += chr(randint(33, 47))  # special symbols
    for _ in range(length_pass - 4):
        password += choice([chr(randint(48, 57)),
                            chr(randint(65, 90)),
                            chr(randint(97, 122)),
                            chr(randint(33, 47))])
    return ''.join(sample(password, k=len(password)))


print(return_numbers("k5k3q2g5z6x9bn"))
print(validate_name())
print(f"Your password is {password_generator()}")
