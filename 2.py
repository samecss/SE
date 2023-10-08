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