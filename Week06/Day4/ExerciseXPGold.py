"""
Exercise 1 : Concatenate Lists
Instructions
Write code that concatenates two lists together without using the + sign.
"""
str1 = "Hello"
str2 = "World!"
str3 = " ".join([str1, str2])
print(str3)  # Hello World!
#  ---------------------------------------------------------------------------
"""
Exercise 2: Greatest Number
Instructions
Ask the user for 3 numbers and print the greatest number.
"""
numbers = []
print("Test Data")
for i in range(3):
    numbers.append(int(input(f"Input the {i+1}{'st' if i == 0 else ('nd' if i == 1 else 'rd')} number: ")))
print(f"The greatest number is: {max(numbers)}")
