base_level = 0
i = 1.6

for year in range(1, 26):
    base_level += i
    if year == 1:
        print("Current ocean level after {} year is  {} mm.".format(year, format(base_level, '.1f')))
    else:
        print("Current ocean level after {} years is  {} mm.".format(year, format(base_level, '.1f')))