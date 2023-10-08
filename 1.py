class Tomato:
    # Статическое свойство со стадиями созревания томатов
    states = ('отсутствует', 'цветение', 'зеленый', 'красный')

    def __init__(self, index):
        # Динамическое свойство, передается параметром
        self._index = index
        # Динамическое свойство, принимает первое значение из списка стадий созревания
        self._state = self.states[0]

    def grow(self):
        # Переводит томат на следующую стадию созревания
        if self._state != self.states[-1]:
            current_state_index = self.states.index(self._state)
            self._state = self.states[current_state_index + 1]

    def is_ripe(self):
        # Проверяет созрел ли томат
        return self._state == self.states[-1]


class TomatoBush:
    def __init__(self, quantity):
        self.tomatoes = []
        # Создает список объектов класса Tomato в зависимости от количества томатов
        for i in range(quantity):
            self.tomatoes.append(Tomato(i))

    def grow_all(self):
        # Переводит все томаты на следующий этап созревания
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        # Возвращает True, если все томаты созрели
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        # Очищает список томатов после сбора урожая
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        # Динамическое свойство, передается параметром
        self.name = name
        # Динамическое свойство, принимает объект класса TomatoBush
        self._plant = plant

    def work(self):
        # Заставляет садовника работать
        self._plant.grow_all()

    def harvest(self):
        # Проверяет, все ли томаты созрели. Если все, то садовник собирает урожай. Если нет, то метод печатает предупреждение
        if self._plant.all_are_ripe():
            print("Мы собрали урожай")
            self._plant.give_away_all()
        else:
            print("Урожай не созрел")


    def knowledge_base():
        # Выводит справку по садоводству
        print("Садовник должен работать. Садовник не работает - урожай не зреет.")


# Вызов справки по садоводству
Gardener.knowledge_base()

# Создание объектов классов TomatoBush и Gardener
tomato_bush = TomatoBush(150)
gardener = Gardener("Садовник", tomato_bush)

# Уход за кустом с помидорами
gardener.work()

# Попытка собрать урожай, когда томаты еще не созрели
gardener.harvest()

# Уход за кустом с помидорами до созревания всех плодов
for i in range(len(Tomato.states)):
    gardener.work()

# Сбор урожая
gardener.harvest()