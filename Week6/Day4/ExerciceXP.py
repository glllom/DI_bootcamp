"""
Exercise 1 : Favorite Numbers
"""
my_fav_numbers = set()
my_fav_numbers.add(21)
my_fav_numbers.add(100)
print(my_fav_numbers)
my_fav_numbers.pop()
print(my_fav_numbers)
friend_fav_numbers = {13, 1000}
print(friend_fav_numbers)
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

"""
Exercise 2: Tuple
Given a tuple which value is integers, is it possible to add more integers to the tuple?
Yes it possible
"""

"""
Exercise 3: Print A Range Of Numbers
Instructions
Use a for loop to print all numbers from 1 to 20, inclusive.

"""
for i in range(20):
    print(i + 1, end=" ")
print()

"""
Exercise 4: Floats
Instructions
Recap – What is a float? What is the difference between an integer and a float?
Can you think of another way to generate a sequence of floats?
Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
"""
my_list = []
for i in range(3, 11):
    my_list.append(i / 2)
print(my_list)

"""
Exercise 5: Shopping List
Instructions
Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

Remove “Banana” from the list.
Remove “Blueberries” from the list.
Add “Kiwi” to the end of the list.
Add “Apples” to the beginning of the list.
Count how many apples are in the basket.
Empty the basket.
Print(basket)
"""
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
print(basket.count("Apples"))
basket = []
print(basket)

"""
Exercise 6 : Loop
Instructions
Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.

"""
my_name = "Gleb"
while input() != my_name:
    print("Wrong name.")

"""
Exercise 7
Instructions
Given a list, use a loop to print out every element which has an even index.
"""
list_to_even = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in list_to_even:
    if not num % 2:
        print(num)

"""
Exercise 8
Instructions
Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.
"""

for num in range(1500, 2500):
    if not num % 5 and not num % 7:
        print(num)
"""
Exercise 9: Favorite Fruits
"""
fruits = input("Input your favorite fruits, separated by single space. ").strip().split(" ")
another_fruit = input("Now, input any fruit ")
if another_fruit in fruits:
    print("You choose one of your favorite fruits! Enjoy! ")
else:
    print("You choose a new fruit. I hope you enjoy.")

"""
Exercise 10: Who Ordered A Pizza ?
Instructions
Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
As they enter each topping, print a message saying you’ll add that topping to their pizza.
Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).
"""
toppings = []
print("Input your toppings. In the end input 'quit'")
topping = input()
while topping != "quit":
    toppings.append(topping)
    print(f"We’ll add {topping} to your pizza.")
    topping = input()
print(f"Total price is: {10 + 2.5 * len(toppings)}")

"""
Exercise 11: Cinemax
"""
total_cost = 0
ages = input("Input your ages, separated by single space. ").strip().split(" ")
for age in ages:
    if 3 <= int(age) <= 12:
        total_cost += 10
    if int(age) < 12:
        total_cost += 15
print(f"Total price is {total_cost}")
