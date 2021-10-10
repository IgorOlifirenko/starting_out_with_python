CLASS_A = 20
CLASS_B = 15
CLASS_C = 10


def main():
    sold_a_tickets = float(input("Билтов класса А продано: "))
    sold_b_tickets = float(input("Билтов класса B продано: "))
    sold_c_tickets = float(input("Билтов класса C продано: "))

    total = get_total_income(sold_a_tickets, sold_b_tickets, sold_c_tickets)

    print(total)


def get_total_income(a, b, c):
    return (a * CLASS_A) + (b * CLASS_B) + (c * CLASS_C)


main()
