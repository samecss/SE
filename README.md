# Тема 5. Базовые коллекции: множества, списки
Отчет по Теме #5 выполнил:
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
### Ресторан на предприятии ведет учет посещений за неделю при помощи кода работника. У них есть список со всеми посещениями за неделю. Ваша задача посчитать:<br>• Сколько было выдано чеков<br>• Сколько разных людей посетило ресторан<br>• Какой работник посетил ресторан больше всех раз.

```python
import collections

workers = [8734, 2345, 8201, 6621, 9999, 1234, 5678, 8201, 8888, 4321, 3365, 1478, 9865,
    5555, 7777, 9998, 1111, 2222, 3333, 4444, 5556, 6666, 5410, 7778, 8889, 4445, 1439,
    9604, 8201, 3365, 7502, 3016, 4928, 5837, 8201, 2643, 5017, 9682, 8530, 3250, 7193,
    9051, 4506, 1987, 3365, 5410, 7168, 7777, 9865, 5678, 8201, 4445, 3016, 4506, 4506
]

common_num = collections.Counter(workers).most_common(1)[0][0]

print("Общее количество чеков:", len(workers))
print("количество чеков без повторов:", len(set(workers)))
print("Посетил больше всего раз:", common_num)
```

### Результат
![Консоль]()

## Выводы
Выполняя задание я узнал как работать со списками, ознакомился с их методами, научился работать с импортированным модулем коллекций, например создавать счетчик без прямого использования цикла или словаря
  
## Самостоятельная работа №2
### На физкультуре студенты сдавали бег, у преподавателя физкультуры есть список всех результатов, ему нужно узнать<br>• Три лучшие результата<br>• Три худшие результата<br>• Все результаты начиная с 10<br>Ваша задача помочь ему в этом.

```python
results = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9,
    27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4
]

results.sort()

print("Тройка лучших:", *results[-3:])
print("Тройка худших:", *results[:3])
print("По возрастанию", *results)
```

### Результат
![Консоль]()

## Выводы
Выполняя задание я узнал как выводить срезы списков, как работает метод сортировки и в чем его отличие от функции sorted. Также научился распаковывать списки.
  
## Самостоятельная работа №3
### Преподаватель по математике придумал странную задачку. У вас есть три списка с элементами, каждый элемент которых – длина стороны треугольника, ваша задача найти площади двух треугольников, составленные из максимальных и минимальных элементов полученных списков.

```python
from math import sqrt

lists = [[12, 25, 3, 48, 71], [5, 18, 40, 62, 98], [4, 21, 37, 56, 84]]


def count_triangle_area(a, b, c):
    p = (a + b + c) / 2
    area = sqrt(p * (p - a) * (p - b) * (p - c))
    return round(area, 1)


for onelist in lists:
    onelist.sort()

min_a, min_b, min_c = min(lists[0]), min(lists[1]), min(lists[2])
max_a, max_b, max_c = max(lists[0]), max(lists[1]), max(lists[2])

if __name__ == "__main__":
    print(f"Площадь меньшего треугольника: {count_triangle_area(min_a, min_b, min_c)}")
    print(f"Площадь большего треугольника: {count_triangle_area(max_a, max_b, max_c)}")
```

### Результат
![Консоль]()

## Выводы
Выполняя задание я узнал как использовать цикл для вложенных списков, выбирать определенные элементы списка и как можно применять функции, когда нужно сделать одни и те же действия с разными аргументами

## Самостоятельная работа №4
### Никто не любит получать плохие оценки, поэтому Борис решил это исправить. Допустим, что все оценки студента за семестр хранятся в одном списке. Ваша задача удалить из этого списка все двойки, а все тройки заменить на четверки.
```python
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
```

### Результат
![Консоль]()

## Выводы
Выполняя задание я узнал как добавлять элементы в список и что сами элементы списка нельзя изменить, только присвоить новое значение, обращаясь к элементу по индексу

  
## Самостоятельная работа №5
### Вам предоставлены списки натуральных чисел, из них необходимо сформировать множества. При этом следует соблюдать это правило: если какое-либо число повторяется, то преобразовать его в строку по следующему образцу: например, если число 4 повторяется 3 раза, то в множестве будет следующая запись: само число 4, строка «44», строка «444».

```python
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
```

### Результат
![Консоль]()

## Выводы
Выполняя задание я узнал как добавлять элементы в множество и что в нем могут храниться данные разных типов


## Общие выводы по теме
Выполняя работы по данной теме я изучил списки и множества, их методы, изменяемость элементов и допустимость хранения одинаковых элементов
