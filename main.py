from math import sqrt


def count_triangle_area(a, b, c):
    p = (a + b + c) / 2
    area = sqrt(p * (p - a) * (p - b) * (p - c))
    print(round(area, 1))