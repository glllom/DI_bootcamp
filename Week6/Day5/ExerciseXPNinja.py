import random

"""
Exercise 1: List Of Integers - Randoms
"""
my_list = [random.randint(-100, 100) for x in range(random.randint(51, 100))]
for num in my_list:
    if num > 0:
        print(*[x for x in range(num) if not x % 2], sep=", ")
    else:
        print(*[x for x in range(0, num, -1) if not x % 2], sep=", ")
#  ------------------------------------------------------------------------------------------------
"""
Exercise 2: Authentication CLI - Login:
"""
users = {'Trump': 'mexican', 'Bennet': 'money', 'Putin': 'weapon'}
input_word = ""
logged_in = ""
while input_word != "exit":
    input_word = input("Type either 'login' or 'exit': ")
    if input_word == "login":
        username, password = input("Enter username: "), input("Enter password: ")
        if username in users and users[username] == password:
            logged_in = username
            print("You are now logged in.")
            break
        elif username not in users:
            print("You are not registered yet. Would you like to register now?")
            input_word = input("Input you username or 'exit': ")
            if input_word != "exit" and input_word not in users:
                users[input_word] = input("Input you password: ")
                print("You are registered now")
                break
        else:
            print("Password is incorrect.")
