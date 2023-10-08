# Тема 7. Работа с файлами (ввод, вывод)
Отчет по Теме #7 выполнил:
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
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.

![Консоль]()

```python
from collections import Counter
from string import punctuation

with open("1.txt", "r") as f:
    text = f.read().split()

words = []
for word in text:
    if len(word) > 2:
        words.append(word.strip(punctuation))

common_word = Counter(words).most_common(1)[0][0]
print(f"Всего слов {len(text)}, чаще встречается слово '{common_word}'.")
```

### Результат
![Консоль]()

## Выводы
Выполняя задание я научился открывать файлы для чтения, заполнять новый список, пользоваться коллекцией для определения топ-1 элемента по числу вхождений
  
## Самостоятельная работа №2
### У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.

```python
def track_spending():
    while True:
        date = input("Введите дату:\n")
        category = input("Введите категорию расхода:\n")
        summ = input("Введите сумму расхода:\n")
        with open("spending.txt", "a") as file:
            file.write(f"{date} ; {category} ; {summ}\n")
        with open("spending.txt", "r") as file:
            print("Записи:\n")
            for line in file:
                print(line.strip())
        choice = int(input("Если хотите ввести ещё запись, нажмите 1\n"))
        if choice != 1:
            break


if __name__ == "__main__":
    track_spending()
```

### Результат
![Консоль]()

## Выводы
Выполняя задание я научился открывать файлы для записи, использовать цикл с логическим условием

## Самостоятельная работа №3
### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.

```python
from collections import Counter

with open("3.txt", "r") as f:
    text = f.read()

num_letters = sum(Counter(filter(str.isalpha, text)).values())
num_words = len(text.split())
num_lines = len(text.splitlines())

print("Количество букв:", num_letters)
print("Количество слов:", num_words)
print("Количество строк:", num_lines)
```

### Результат
![Консоль]()

## Выводы
Выполняя задание я научился подсчитывать количество с помощью функции filter модуля collections чтобы считать только буквенные символы, далее с помощью подсчета вхождений каждой буквы функцией Counter и суммирования полученных значений

## Самостоятельная работа №4
### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****.

```python
with open("4.txt", "r") as f:
    bad_words = f.read().split()

string = "Hello, world! Python IS the programming language of thE future. My EMAIL is....PYTHON is awesome!!!!".split()

final_string = ""
for word in string:
    censored_word = word
    tmp = censored_word.lower()
    for bad_word in bad_words:
        if bad_word in tmp:
            censored_word = tmp.replace(bad_word, "*" * len(bad_word))
    final_string += censored_word + " "
print(final_string)
```

### Результат
![Консоль]()

## Выводы
Выполняя задание я проодлжил изучение возможностей строк, например объединил замену методом replace и умножение строки на количество необходимых повторений, узнал как можно не меняя исходную строку использовать изменение регистра

## Самостоятельная работа №5
### Дан текстовый файл "5.csv", содержащий информацию о студентах: ФИО студента, оценки или буквы "б" и "н". Напишите программу, которая считывает данные из файла и выводит на экран фамилии студентов, имеющих больше двух "н".

```python
import csv

with open("5.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        name = row[0]
        grades = row[1:]
        if grades.count("н") > 2:
            print(name)
```

### Результат
![Консоль]()

## Выводы
Выполняя задание я узнал как работать и открывать для чтения файлы формата csv


## Общие выводы по теме
Выполняя работы по данной теме я узнал как робоать с разными типами файлов для чтения и записи, как интегрировать данные из них в код и работать с их содержимым
