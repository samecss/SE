class Bird:
    def __init__(self, name, family):
        self.name = name
        self.family = family

    def get_name_and_family(self):
        print(
            f"Птица {self.name.capitalize()} относится к семейству {self.family.capitalize()}."
        )

    def describe_appearance(self):
        print("Для птицы не заведено описание внешности.")


class Anatidae(Bird):
    def __init__(self, name, family, beak_color, legs_color):
        super().__init__(name, family)
        self._beak_color = beak_color
        self.legs_color = legs_color

    def describe_appearance(self):
        print(
            f"У птицы {self.name.capitalize()} клюв {self._beak_color}, ноги {self.legs_color}."
        )

    def change_beak_color(self, beak_color):
        self._beak_color = beak_color


bird = Anatidae("савка", "утиные", "голубой", "серые")
bird.get_name_and_family()
bird.change_beak_color("серый")
bird.describe_appearance()
bird = Bird("голубь", "голубиные")
bird.get_name_and_family()
bird.describe_appearance()