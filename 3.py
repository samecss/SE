from math import sqrt

lists = [[12, 25, 3, 48, 71], [5, 18, 40, 62, 98], [4, 21, 37, 56, 84]]


def count_triangle_area(a, b, c):
    p = (a + b + c) / 2
    area = sqrt(p * (p - a) * (p - b) * (p - c))
    return round(area, 1)


min_a, min_b, min_c = min(lists[0]), min(lists[1]), min(lists[2])
max_a, max_b, max_c = max(lists[0]), max(lists[1]), max(lists[2])

if __name__ == "__main__":
    print(f"Площадь меньшего треугольника: {count_triangle_area(min_a, min_b, min_c)}")
    print(f"Площадь большего треугольника: {count_triangle_area(max_a, max_b, max_c)}")