def main():
    print("Введите месячныетраты:")
    input("Нажмите Enter, чтобы продолжить.")

    monthly_cost = get_monthly_costs()

    cost_per_year = get_year_costs(monthly_cost)

    print("Общая месячная сумма - ${}.".format(format(monthly_cost, '.2f')))
    print("Общая годовая сумма - ${}.".format(format(cost_per_year, '.2f')))


def get_monthly_costs():
    loan_payment = float(input("Платеж по кредиту: "))

    insurance = float(input("Страховка: "))
    fuel = float(input("Стоимость топлива: "))
    motor_oil = float(input("Стоимость машинного масла: "))
    tires = float(input("Стоимость покрышек: "))
    maintenance = float(input("Стоимость техобслуживания: "))

    return loan_payment + insurance + fuel + motor_oil + tires + maintenance


def get_year_costs(cost_for_months):
    return cost_for_months * 12


main()