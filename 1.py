numbers = input("Введите числа через пробел:\n")

numbers = numbers.split()

numbers_list = list(map(int, numbers))
numbers_tuple = tuple(numbers_list)

print("Список:", numbers_list)
print("Кортеж:", numbers_tuple)