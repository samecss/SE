def summing():
    try:
        x = int(input()) + 2
        print(x)
    except ValueError:
        print(Exception("Неподходящий тип данных. Ожидалось число."))


if __name__ == "__main__":
    summing()