with open("4.txt", "r") as f:
    bad_words = f.read().split()

string = '''Hello, world! Python IS the programming language of thE future. My
EMAIL is....
PYTHON is awesome!!!!'''.split()

final_string = ""
for word in string:
    censored_word = word
    tmp = censored_word.lower()
    for bad_word in bad_words:
        if bad_word in tmp:
            censored_word = tmp.replace(bad_word, "*" * len(bad_word))
    final_string += censored_word + " "
print(final_string)