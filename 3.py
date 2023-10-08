from collections import Counter

string = input()
numbers = []


def count_numbers(string):
    for i in string:
        numbers.append(int(i))
    counter = Counter(string)
    sorted_counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    top_3 = dict(sorted_counter[:3])
    result = dict(sorted(top_3.items()))
    print(result)


if __name__ == "__main__":
    count_numbers(string)