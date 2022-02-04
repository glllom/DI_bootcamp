# import re
# """
# Exercise 1: Birthday Look-Up
# """
#
# birthdays = {"Elizabeth II, Queen of the United Kingdom": "1926/04/21", "Charles, Prince of Wales": "1948/11/14",
#              "Diana, Princess of Wales": "1961/07/01", "Prince William, Duke of Cambridge": "1982/04/29",
#              "Prince Henry, Duke of Sussex": "1984/08/15"}
#
# print("Welcome, dear user.")
# print("You can add your birthday to the list.")
# print("To add your birthday, please input your name and your birthday (YYYY/MM/DD) separate by space.")
# print("When you finish, input 'end' in new line.")
# while True:
#     new_person = input().split(",")
#     if new_person == ["end"]:
#         break
#     if len(new_person) != 2:
#         print("Incorrect input")
#         continue
#     if re.fullmatch(r'\d{4}/\d{2}/\d{2}', new_person[1].strip()) is None:
#         print("Incorrect date")
#         continue
#     if new_person[0] in birthdays:
#         print(f"{new_person[0]} already in list. His birthday in {birthdays[new_person[0]]}")
#     else:
#         birthdays[new_person[0]] = new_person[1]
# print("You can look up the birthdays of the people in the list!")
# print("Choose a number of a person to see his Birthdate:")
# for index, person in enumerate(birthdays.keys()):
#     print(index+1, '). ', person, sep='')
# choice = input("Your choice: ")
# if not choice.isdigit():
#     print(f"Sorry, we don’t have the birthday information for {choice}")
# elif int(int(choice)-1) not in range(len(birthdays)):
#     print("Sorry, incorrect choice")
# else:
#     print(f"{list(birthdays)[int(choice)-1]} was born in {birthdays[list(birthdays)[int(choice)-1]]}")
#  -------------------------------------------------------------------------------------------------------
"""
Exercise 4: Fruit Shop
"""
items = {"banana": 4,
         "apple": 2,
         "orange": 1.5,
         "pear": 3}
for fruit, price in items.items():
    print(f"{fruit} costs ${price}.")
    