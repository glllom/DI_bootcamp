str_list = input("Give me a string: ").strip().split(" ")
dict = {}
while len(str_list):
    if str_list[0] in dict:
        dict[str_list[0]] += 1
    else:
        dict[str_list[0]] = 1
    str_list.pop(0)
for key, value in dict.items():
    print(key, value, sep=": ")

