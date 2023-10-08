tuples = ((1, 2, 3), (1, 8, 3, 4, 8, 8, 9, 2), (1, 2, 8, 5, 1, 2, 9))
x = int(input("Введите номер сотрудника:\n"))


def find_start_end(onetuple, x):
    if x not in onetuple:
        print(tuple())
    elif onetuple.count(x) == 1:
        print(onetuple[onetuple.index(x) :])
    else:
        last = onetuple.index(x, onetuple.index(x) + 1)
        print(onetuple[onetuple.index(x) : last + 1])


if __name__ == "__main__":
    for onetuple in tuples:
        find_start_end(onetuple, x)