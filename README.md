# Тема 2. Базовые операции языка Python
Отчет по Теме #2 выполнил:
- Рожков Сергей Сергеевич
- ЗПИЭ-20-2

| Задание | Сам_раб |
| ------  | ------ |
| Задание 1 | + |
| Задание 2 | + |
| Задание 3 | + |
| Задание 4 | + |
| Задание 5 | + |
| Задание 6 | + |
| Задание 7 | + |
| Задание 8 | + |
| Задание 9 | + |
| Задание 10 | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Самостоятельная работа №1
### Выведите в консоль булевую переменную False, не используя слово False в строке или изначально присвоенную булевую переменную. Программа должна занимать не более двух строк редактора кода.

```python
print(1 > 2)
```

## Результат
![Консоль](https://github.com/samecss/SE/blob/ae7df83f534c4fc9d86f474259b38e140f928b75/images/1.png)

## Выводы
Выполняя задание я узнал, что логическая переменная может выводиться с помощью операторов сравнения

## Самостоятельная работа №2
### Присвоить значения трем переменным и вывести их в консоль, используя только две строки редактора кода.

```python
a, b, c = 2, 4, 6
print(a, b, c, sep=", ")
```

## Результат
![Консоль](https://github.com/samecss/SE/blob/ae7df83f534c4fc9d86f474259b38e140f928b75/images/2.png)

## Выводы
Выполняя задание я узнал, что переменные можно объявить одной строкой, а вывод можно дополнить аргументом, разделяющим переменные какой угодно строкой
  
## Самостоятельная работа №3
### Реализуйте ввод данных в программу, через консоль, в виде только целых чисел (тип данных int). То есть при вводе буквенных символов в консоль, программа не должна работать. Программа должна занимать не более двух строк редактора кода.

```python
x = int(input())
print("Число", x)
```

## Результат
![Консоль](https://github.com/samecss/SE/blob/ae7df83f534c4fc9d86f474259b38e140f928b75/images/3.1.png)
![Консоль](https://github.com/samecss/SE/blob/ae7df83f534c4fc9d86f474259b38e140f928b75/images/3.2.png)

## Выводы
Выполняя задание я узнал, что тип данных в питоне можно указать напрямую
  
## Самостоятельная работа №4
### Создайте только одну строковую переменную. Длина строки должна не превышать 5 символов. На выходе мы должны получить строку длиной не менее 16 символов. Программа должна занимать не более двух строк редактора кода.

```python
x = input()
print(x * (16 // len(x[:5]) + 1))
```

## Результат
![Консоль](https://github.com/samecss/SE/blob/ae7df83f534c4fc9d86f474259b38e140f928b75/images/4.png)

## Выводы
Выполняя задание я узнал, что к строкам можно применять срезы, а умножение строки на число даёт повторение строки столько раз, чему равняется число
  
## Самостоятельная работа №5
### Создайте три переменные: день (тип данных - числовой), месяц (тип данных - строка), год (тип данных - числовой) и выведите в консоль текущую дату в формате: “Сегодня день месяц год. Всего хорошего!” используя F строку и оператор end внутри print(), в котором вы должны написать фразу “Всего хорошего!”. Программа должна занимать не более двух строк редактора кода.

```python
day, month, year = int(input("Введите день")), input("Введите месяц"), int(input("Введите год"))
print(f"Сегодня {day} {month} {year} ", end="Всего хорошего!")
```

## Результат
![Консоль](https://github.com/samecss/SE/blob/ae7df83f534c4fc9d86f474259b38e140f928b75/images/5.png)

## Выводы
Выполняя задание я узнал, что объявлять переменные в одну строку можно и с переменными разных типов данных, а вывод строки может с помощью аргумента end заканчивать вывод какой угодно строкой
  
## Самостоятельная работа №6
### В предложении ‘Hello World’ вставьте ‘my’ между двумя словами. Выведите полученное предложение в консоль в одну строку. Программа должна занимать не более двух строк редактора кода.

```python
hw = "Hello World"
print(hw.replace(" ", "my"))
```

## Результат
![Консоль](https://github.com/samecss/SE/blob/ae7df83f534c4fc9d86f474259b38e140f928b75/images/6.png)

## Выводы
Выполняя задание я узнал, что применяя метод строки replace можно заменить вхождения подстроки в строке на новую подстроку 
  
## Самостоятельная работа №7
### Узнайте длину предложения ‘Hello World’, результат выведите в консоль. Программа должна занимать не более двух строк редактора кода.

```python
print("Длина", len("Hello World"))
```

## Результат
![Консоль](https://github.com/samecss/SE/blob/ae7df83f534c4fc9d86f474259b38e140f928b75/images/7.png)

## Выводы
Выполняя задание я узнал, что функция len может посчитать длину строки
  
## Самостоятельная работа №8
### Переведите предложение ‘HELLO WORLD’ в нижний регистр. Программа должна занимать не более двух строк редактора кода.

```python
hw = "HELLO WORLD"
print(hw.lower())
```

## Результат
![Консоль](https://github.com/samecss/SE/blob/ae7df83f534c4fc9d86f474259b38e140f928b75/images/8.png)

## Выводы
Выполняя задание я узнал, что метод lower может изменить регистр строки
  
## Самостоятельная работа №9
### Вводится целое число. Для вывода должно быть вычислено следующее за ним четное число.

```python
x = int(input("Введите число:\n"))
print("Результат:", (x // 2 + 1) * 2, sep="\n")
```

## Результат
![Консоль](https://github.com/samecss/SE/blob/ae7df83f534c4fc9d86f474259b38e140f928b75/images/9.png)

## Выводы
Выполняя задание я повторил основные базовые арифметические операции над целыми числами

  
## Самостоятельная работа №10
### Вводится строка. Выводятся все символы строки, расположенные по четным индексам.

```python
x = input("Введите строку:\n")
print("Результат:", x[0::2], sep="\n")
```

## Результат
![Консоль](https://github.com/samecss/SE/blob/ae7df83f534c4fc9d86f474259b38e140f928b75/images/10.png)

## Выводы
Выполняя задание я узнал, что срезы могут быть не только в диапазоне "от-до", но и с неким заданным шагом

## Общие выводы по теме
Выполняя работы по данной теме я изучил типы данных строки, числа, логический тип, научился базовым операциям, методам строк, срезам
