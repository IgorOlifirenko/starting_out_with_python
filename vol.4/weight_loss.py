lost_wight = 1.5

start_weight = float(input("Enter your current weight: "))

for month in range(1, 6):
    start_weight -= lost_wight
    print("Your weight after {} months will be {} kg.".format(month, start_weight))
