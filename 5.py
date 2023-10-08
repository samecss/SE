import csv

with open("5.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        name = row[0]
        grades = row[1:]
        if grades.count("н") > 2:
            print(name)