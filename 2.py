tuples = ((1, 2, 3), (1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), (2, 4, 6, 6, 4, 2))
x = int(input("Введите число, которое хотите удалить:\n"))


def delete_first(onetuple, x):
    onelist = list(onetuple)
    if x in onelist:
        onelist.remove(x)
        return "Произведено удаление:", tuple(onelist)
    else:
        return "Кортеж без изменений:", onetuple


if __name__ == "__main__":
    for onetuple in tuples:
        print(*delete_first(onetuple, x))