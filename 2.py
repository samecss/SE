class Bird:
    def __init__(self, name, family):
        self.name = name
        self.family = family

    def get_name_and_family(self):
        print(
            f"Птица {self.name.capitalize()} относится к семейству {self.family.capitalize()}."
        )


bird = Bird("савка", "утиные")
bird.get_name_and_family()