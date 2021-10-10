FEDERAL_TAX = 0.05
REGIONAL_TAX = 0.025


def main():
    purchase_size = float(input("Введите сумму покупки: "))

    fed_tax = get_federal_tax(purchase_size)

    reg_tax = get_regional_tax(purchase_size)

    total_tax = fed_tax + reg_tax

    amount = purchase_size + total_tax

    print("Сумма покупки: $", format(purchase_size, '.2f'), sep='')
    print(f"Федеральный налог ({FEDERAL_TAX * 100}%): $", format(fed_tax, '.2f'), sep='')
    print(f"Регионалальный налог ({REGIONAL_TAX * 100}%): $", format(reg_tax, '.2f'), sep='')
    print("Общая сумма покупки: $", format(amount, '.2f'), sep='')


def get_federal_tax(purchase):
    return purchase * FEDERAL_TAX


def get_regional_tax(purchase):
    return purchase * REGIONAL_TAX


main()
