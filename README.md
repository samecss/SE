# Тема 11. Итераторы и генераторы
Отчет по Теме #11 выполнил:
- Рожков Сергей Сергеевич
- ЗПИЭ-20-2

| Задание | Сам_раб |
| ------  | ------ |
| Задание 1 | + |
| Задание 2 | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Самостоятельная работа №1
### Вас никак не могут оставить числа Фибоначчи, очень уж они вас заинтересовали. Изучив новые возможности Python вы решили реализовать программу, которая считает числа Фибоначчи при помощи итераторов. Расчет начинается с чисел 1 и 1. Создайте функцию fib(n), генерирующую n чисел Фибоначчи с минимальными затратами ресурсов. Для реализации этой функции потребуется обратиться к инструкции yield (Она не сохраняет в оперативной памяти огромную последовательность, а дает возможность “доставать” промежуточные результаты по одному). Результатом решения задачи будет листинг кода и вывод в консоль с числом Фибоначчи от 200.

```python
def fib(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b


fib_numbers = list(fib(1001))
print(*fib_numbers, sep="\n")
```

### Результат
![Консоль]()

## Выводы
Выполняя задание я узнал, что после yield возможно дальнейшее выполнение кода из-за того, что на этом моменте происходит приостановка и проверка - продолжает ли функция выполнение, и если да, то итерация идёт дальше, переходя к следующей строчке после yield

## Самостоятельная работа №2
### К коду предыдущей задачи добавьте запоминание каждого числа Фибоначчи в файл “fib.txt”, при этом каждое число должно находиться на отдельной строчке. Результатом выполнения задачи будет листинг кода и скриншот получившегося файла

```python
def fib(n):
    a, b = 1, 1
    with open("fib.txt", "w") as f:
        for i in range(n):
            f.write(str(a) + "\n")
            yield a
            a, b = b, a + b


fib_numbers = list(fib(1001))
print(*fib_numbers, sep="\n")
```

### Результат
![Консоль]()

## Выводы
Выполняя задание я узнал как производить запись в текстовый файл построчно
  
## Общие выводы по теме
Выполняя работы по данной теме я изучил yield, последовательно возвращающий значения в виде генератора
