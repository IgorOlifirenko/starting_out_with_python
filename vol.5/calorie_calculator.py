def main():
    print("Введите колличество грамм жиров и углеводов, которые вы употребили за день.")
    fats = float(input("Колличство грамм жиров: "))
    carbs = float(input("Колличство грамм углводов: "))

    calorie_from_fats = get_calorie_from_fats(fats)

    calorie_from_carbs = get_calorie_from_carbs(carbs)

    print("Колличество каллорий от жиров: {} ккал.".format(format(calorie_from_fats, '.1f')))
    print("Колличество каллорий от углеводов: {} ккал.".format(format(calorie_from_carbs, '.1f')))


def get_calorie_from_fats(fats):
    return fats * 9


def get_calorie_from_carbs(carbs):
    return carbs * 4


main()
