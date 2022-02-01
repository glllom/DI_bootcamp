list1 = [5, 10, 15, 20, 25, 50, 20]
for i in range(len(list1)):
    if list1[i] == 20:
        list1[i] = 200
        break
print(list1)

aTuple = (10, 20, 30, 40)

first, second, third, forth = aTuple
print(first, second, third, forth)
