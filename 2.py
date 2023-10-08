for file in ["empty.txt", "spending.txt"]:
    try:
        with open(file, "r") as f:
            content = f.read()
        if not content.strip():
            raise Exception("Файл пустой")
        print(content)
    except Exception as warning:
        print(warning)