x = int(input('Enter the Number:'))
print(x == sum(num for num in range(1, x) if x % num == 0))