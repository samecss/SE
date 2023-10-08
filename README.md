# Тема 8. Введение в ООП
Отчет по Теме #8 выполнил:
- Рожков Сергей Сергеевич
- ЗПИЭ-20-2

| Задание | Сам_раб |
| ------  | ------ |
| Задание 1 | + |
| Задание 2 | + |
| Задание 3 | + |
| Задание 4 | + |
| Задание 5 | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Самостоятельная работа №1
### Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Bird:
    print("Утка это Птица")


duck = Bird()
```

### Результат
![Консоль](https://github.com/samecss/SE/blob/9806c2791818362458d13e66fb3d83e75a466e8b/%D1%81%D0%BA%D1%80%D0%B8%D0%BD%D1%8B/1.png)

## Выводы
Выполняя задание я научился создавать класс и объект класса без атрибутов

## Самостоятельная работа №2
### Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Bird:
    def __init__(self, name, family):
        self.name = name
        self.family = family

    def get_name_and_family(self):
        print(
            f"Птица {self.name.capitalize()} относится к семейству {self.family.capitalize()}."
        )


bird = Bird("савка", "утиные")
bird.get_name_and_family()
```

### Результат
![Консоль](https://github.com/samecss/SE/blob/9806c2791818362458d13e66fb3d83e75a466e8b/%D1%81%D0%BA%D1%80%D0%B8%D0%BD%D1%8B/2.png)

## Выводы
Выполняя задание я научился создавать атрибуты (в данном случае название и семейство птиц) и метод класса, выводящий атрибуты в виде справки о птице
  
## Самостоятельная работа №3
### Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Bird:
    def __init__(self, name, family):
        self.name = name
        self.family = family

    def get_name_and_family(self):
        print(
            f"Птица {self.name.capitalize()} относится к семейству {self.family.capitalize()}."
        )


class Anatidae(Bird):
    def __init__(self, name, family, beak_color, legs_color):
        super().__init__(name, family)
        self.beak_color = beak_color
        self.legs_color = legs_color

    def describe_appearance(self):
        print(
            f"У птицы {self.name.capitalize()} клюв {self.beak_color}, ноги {self.legs_color}."
        )

bird = Anatidae("пеганка", "утиные", "ярко-красный", "розовые")
bird.get_name_and_family()
bird.describe_appearance()
bird = Anatidae("савка", "утиные", "голубой", "серый")
bird.get_name_and_family()
bird.describe_appearance()
```

### Результат
![Консоль](https://github.com/samecss/SE/blob/9806c2791818362458d13e66fb3d83e75a466e8b/%D1%81%D0%BA%D1%80%D0%B8%D0%BD%D1%8B/3.png)

## Выводы
Выполняя задание я научился создавать наследственный класс (в данном случае семейство утиных) со своими собственными атрибутами (цвета ног и клюва), и выводить информацию, вызывая метод родительского класса в наследственном

## Самостоятельная работа №4
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Bird:
    def __init__(self, name, family):
        self.name = name
        self.family = family

    def get_name_and_family(self):
        print(
            f"Птица {self.name.capitalize()} относится к семейству {self.family.capitalize()}."
        )


class Anatidae(Bird):
    def __init__(self, name, family, beak_color, legs_color):
        super().__init__(name, family)
        self._beak_color = beak_color
        self.legs_color = legs_color

    def describe_appearance(self):
        print(
            f"У птицы {self.name.capitalize()} клюв {self._beak_color}, ноги {self.legs_color}."
        )

    def change_beak_color(self, beak_color):
        self._beak_color = beak_color


bird = Anatidae("пеганка", "утиные", "ярко-красный", "розовые")
bird.get_name_and_family()
bird.describe_appearance()
bird = Anatidae("савка", "утиные", "голубой", "серые")
bird.get_name_and_family()
bird.describe_appearance()

bird.change_beak_color("серый")
bird.describe_appearance()
```

### Результат
![Консоль](https://github.com/samecss/SE/blob/9806c2791818362458d13e66fb3d83e75a466e8b/%D1%81%D0%BA%D1%80%D0%B8%D0%BD%D1%8B/4.png)

## Выводы
Выполняя задание я научился инкапсулировать атрибуты (в данном случае цвет клюва в наследственном классе) и использовать метод класса для изменения атрибута внутри класса, мной был выбран атрибут "цвет клюва" так как его цвет может меняться в зависимости от сезона, но не у всех и не всегда.

## Самостоятельная работа №5
### Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Bird:
    def __init__(self, name, family):
        self.name = name
        self.family = family

    def get_name_and_family(self):
        print(
            f"Птица {self.name.capitalize()} относится к семейству {self.family.capitalize()}."
        )

    def describe_appearance(self):
        print("Для птицы не заведено описание внешности.")


class Anatidae(Bird):
    def __init__(self, name, family, beak_color, legs_color):
        super().__init__(name, family)
        self._beak_color = beak_color
        self.legs_color = legs_color

    def describe_appearance(self):
        print(
            f"У птицы {self.name.capitalize()} клюв {self._beak_color}, ноги {self.legs_color}."
        )

    def change_beak_color(self, beak_color):
        self._beak_color = beak_color


bird = Anatidae("савка", "утиные", "голубой", "серые")
bird.get_name_and_family()
bird.change_beak_color("серый")
bird.describe_appearance()
bird = Bird("голубь", "голубиные")
bird.get_name_and_family()
bird.describe_appearance()
```

### Результат
![Консоль](https://github.com/samecss/SE/blob/9806c2791818362458d13e66fb3d83e75a466e8b/%D1%81%D0%BA%D1%80%D0%B8%D0%BD%D1%8B/5.png)

## Выводы
Выполняя задание я научился реализовывать полиморфизм в коде, теперь метод, описывающий у утиных цвет ног и клюва, возвращает разную информацию в зависимости от класса объекта

## Общие выводы по теме
Выполняя работы по данной теме я узнал, как с помощью ООП создавать код, который можно изменять и расширять под свои потребности. Изучил основные составляющие: атрибуты, классы, объекты. Основные возможности: как скрывать элементы кода, создавать новые классы основываясь на существующих, создавать разное поведение для объектов.
