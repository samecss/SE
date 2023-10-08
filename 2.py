def fib(n):
    a, b = 1, 1
    with open("fib.txt", "w") as f:
        for i in range(n):
            f.write(str(a) + "\n")
            yield a
            a, b = b, a + b


fib_numbers = list(fib(1001))
print(*fib_numbers, sep="\n")