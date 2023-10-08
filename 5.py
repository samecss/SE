products = [("Чай", 150, 5), ("Кофе", 400, 3), ("Сахар", 90, 7), ("Корица", 200, 10)]

price = int(input("Введите цену:\n"))
amount = int(input("Введите количество:\n"))

print("Список доступных товаров:")
for product in products:
    if product[1] <= price and product[2] >= amount:
    	print(product[0])