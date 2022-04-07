"""
Exercise 1 : Hello World
"""
print("Hello World\nHello World\nHello World\nHello World")
# ----------------------------------------------------------------
"""
Exercise 2 : Some Math
"""
print((99 ** 3) * 8)
# ----------------------------------------------------------------
"""
Exercise 3 : What Is The Output ?

>>> 5 < 3   --> True
>>> 3 == 3  --> True  
>>> 3 == "3"    --> False
>>> "3" > 3    --> Error
>>> "Hello" == "hello"    --> False
"""
# ----------------------------------------------------------------
"""
Exercise 4 : Your Computer Brand
"""
computer_brand = "'Dell'"
print(f"I have a {computer_brand} computer")
# ----------------------------------------------------------------
"""
Exercise 5 : Your Information
"""
name = "Gleb"
age = 39
shoe_size = 44
info = f"Hi, my name is {name}, I am {age} years old, and my shoe size is {shoe_size}"
print(info)
# ----------------------------------------------------------------
"""
Exercise 6 : A & B
"""
a = 20
b = 10
if a > b:
    print("Hello, World")
# ----------------------------------------------------------------
"""
Exercise 7 : Odd Or Even
"""
if int(input("Give me a number: ")) % 2:
    print("This number is odd")
else:
    print("This number is even")
# ----------------------------------------------------------------
"""
Exercise 8 : What’s Your Name ?
"""
my_name = "Paul McCartney"
if input("What’s your name? ") == my_name:
    print("Are you original or double? :-)))")
else:
    print(f"I want to meet you with {my_name}")
# ----------------------------------------------------------------
"""
Exercise 9 : Tall Enough To Ride A Roller Coaster
"""
if int(input("Tell me your height in inches: ")) > 145 / 2.54:  # cm to inches
    print("You are tall enough to ride.")
else:
    print("You need to grow some more to ride.")
