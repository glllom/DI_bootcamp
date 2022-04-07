def fib(number):
    a, b = 0, 1
    for _ in range(number):
        yield a
        a, b = b, a + b


print(*fib(20))
