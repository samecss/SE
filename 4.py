x = list(input().split())


def avrge(args):
    numbers = [int(i) for i in args]
    result = sum(numbers) / len(numbers)
    print(result)


if __name__ == "__main__":
    avrge(x)