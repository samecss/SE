from collections import Counter
from string import punctuation

with open("1.txt", "r",encoding="utf-8") as f:
    text = f.read().split()

words = []
for word in text:
    if len(word) > 2:
        words.append(word.strip(punctuation))

common_word = Counter(words).most_common(1)[0][0]
print(f"Всего слов {len(text)}, чаще встречается слово '{common_word}'.")