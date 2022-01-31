import random
my_str = input("Give me a string 10 characters long: ")

while len(my_str) != 10:
    if len(my_str) < 10:
        print("string not long enough")
    if len(my_str) > 10:
        print("string too long")
    my_str = input("Give me a string 10 characters long: ")
for i in range(len(my_str)):
    print(my_str[:i+1])

lst = (list(my_str))
random.shuffle(lst)
print("".join(lst))

