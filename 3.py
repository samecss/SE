from collections import Counter

with open("3.txt", "r") as f:
    text = f.read()

num_letters = sum(Counter(filter(str.isalpha, text)).values())
num_words = len(text.split())
num_lines = len(text.splitlines())

print("Количество букв:", num_letters)
print("Количество слов:", num_words)
print("Количество строк:", num_lines)