import random


def throw_dice():
    dice_num = random.randint(1, 6)
    if dice_num == 1 or dice_num == 2:
        print("Вы проиграли")
    elif dice_num == 5 or dice_num == 6:
        print("Вы выиграли")
    else:
        print("Выпало 3 или 4. Повторный бросок.")
        throw_dice()


if __name__ == "__main__":
    throw_dice()