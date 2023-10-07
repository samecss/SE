from collections import Counter

x = input()
letters = ["a", "o", "u", "e", "i"]
counter = sum(Counter(x.lower())[letter] for letter in letters)

print('Длина предложения:', len(x))
print('Перевод регистра:', x.lower())
print('Количество гласных:', counter)
print('Замена слов:', x.lower().replace("ugly", "beauty"))
print('Начало и конец предложения:', x.startswith("The") and x.endswith("end"))