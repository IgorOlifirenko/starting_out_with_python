PERCENTAGE = 0.8


def main():
    cost = float(input("Стоимость недвижимости: "))

    result = insurance_cost(cost)

    print(f"Минимальная страховая сумма, при стоимости недвижимости в ${format(cost, ',.2f')} "
          f"составляет ${format(result, ',.2f')}.")


def insurance_cost(cost):
    return cost * PERCENTAGE


main()
