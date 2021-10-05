import sys

while True:
    try:
        n = int(input("Enter positive number: "))

        while n < 0:
            print("Error: your enter negative number, please, try again.")
            n = int(input("Enter positive number: "))

        result = 1

        for i in range(1, n + 1):
            result *= i

        print(result)

        sys.exit(0)
    except ValueError:
        print("Error: your enter a string.")
        n = int(input("Enter positive number, not string: "))
        while n < 0:
            print("Error: your enter negative number, please, try again.")
            n = int(input("Enter positive number: "))

        result = 1

        for i in range(1, n + 1):
            result *= i

        print(result)

        sys.exit(0)
