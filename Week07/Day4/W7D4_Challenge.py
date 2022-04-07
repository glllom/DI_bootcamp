def division(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print("You can not divide by zero! Error -- ", e)


print(division(5, 0))
