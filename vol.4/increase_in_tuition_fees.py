
semester_fee = 45000

for year in range(1, 6):
    semester_fee += semester_fee * 0.03
    print("Semester fee after {} years is {}".format(year, format(semester_fee, '.2f')))
