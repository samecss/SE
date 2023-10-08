# Ввод пользователем навзания птицы
bird_name = input("Введите название птицы, например 'пеганка':\n")

# Объявление словарей с семействами птиц и описанием птиц
bird_family = {
    "Утиные": ["Савка", "Пеганка"],
    "Дятловые": ["Большой пестрый дятел", "Зеленый дятел"],
    "Данные отсутствуют": [],
}

bird_description = {
    "Савка": "голубой клюв, окраска тела состоит из сочетания темно-рыжего, бурого, коричневого и охристого цветов",
    "Пеганка": "ярко-красный клюв, черная с зеленым металлическим отливом голова",
    "Данные отсутствуют": [],
}

# Объявление декоратора для вывода информации о птицах, которая также перехватывает исключения KeyError
def bird_info_decorator(func):
	# Объявление функции-оболочки, которая вызывает исходную функцию
    def wrapper():
        try:
            print("Информация о птице:")
            func(bird_name.lower().capitalize())
        except KeyError:
            print("Название птицы отсутствует в базе")
    return wrapper

# Объявление функции для получения семейства птицы
@bird_info_decorator
def get_bird_family(name):
		# Если название птицы есть в словаре, то выводится семейство и происходит возврат из функции, если нет, то выводится "Данные отсутствуют"
    for family, birds in bird_family.items():
        if name in birds:
            print("Птица относится к семейству", family)
            return
		# Вызывает исключение KeyError если названия птицы нет в словаре
    raise KeyError("Название птицы отсутствует в базе")

# Объявление функции для получения описания птицы
@bird_info_decorator
def get_bird_description(name):
		# Если название птицы есть в словаре, то выводится описание и происходит возврат из функции, если нет, то выводится "Описание недоступно"
    for birds, description in bird_description.items():
        if name in birds:
            print("Имеет", description)
            return
		# Вызывает исключение KeyError если названия птицы нет в словаре
    raise KeyError("Название птицы отсутствует в базе")

# Вызов функций для получения семейства птиц и описания птицы
get_bird_family()
get_bird_description()