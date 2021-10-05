population = int(input("Enter starting number of population: "))
increasing = int(input("Enter average daily increase: ")) / 100
days = int(input("Enter number of days: "))
tab = "\t" * 2
print("Day" + " \t" + "Population")
print("------------------")

for day in range(1, days + 1):
    print(day, tab, format(population, '.1f'))
    population += population * increasing

