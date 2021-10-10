ESTIMATED_COST_INDEX = 0.6
TAX = 72


def main():
    cost = float(input("Введите фактическую стоимость недвижимости: "))

    estimated_cost = get_estimated_cost(cost)

    print("Оценочная стоимость недвижимости: ${}".format(format(estimated_cost, '.2f')))

    tax = tax_calc(estimated_cost)

    print("Налог на имущество: ${}".format(format(tax, '.2f')))


def tax_calc(estimated_cost):
    return estimated_cost / 10000 * TAX


def get_estimated_cost(cost):
    return cost * ESTIMATED_COST_INDEX


main()
