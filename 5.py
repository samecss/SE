def create_sets(onelist):
    result = set(onelist)
    for element in onelist:
        count = onelist.count(element)
        if count > 1:
            for i in range(2, count + 1):
                result.add(str(element) * i)
    print(result)


lists = [[1, 1, 3, 3, 1], [5, 5, 5, 5, 5, 5, 5], [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]]


if __name__ == "__main__":
    for onelist in lists:
        create_sets(onelist)