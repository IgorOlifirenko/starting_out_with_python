def main():
    dist_in_km = float(input("Enter distance in kilometers: "))

    dist_in_miles = kilometers_converter(dist_in_km)

    print(f"{dist_in_km} km is {format(dist_in_miles, '.1f')} miles.")


def kilometers_converter(kilometers):
    return kilometers * 0.6214


main()

