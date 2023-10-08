def fib(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b


fib_numbers = list(fib(1001))
print(*fib_numbers, sep="\n")