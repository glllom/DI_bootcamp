def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("You can not divide by zero!")


print(division(5, 0))
