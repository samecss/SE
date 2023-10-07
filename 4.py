lists = [
    [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4],
    [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4],
    [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4],
]


def correct_grades(onelist):
    for i in onelist:
        onelist.remove(2) if 2 in onelist else None
    for i in range(len(onelist)):
        if onelist[i] == 3:
            onelist[i] = 4
            continue

    print("Обновленные оценки:", onelist)


if __name__ == "__main__":
    for onelist in lists:
        correct_grades(onelist)