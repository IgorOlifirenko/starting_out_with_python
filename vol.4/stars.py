base = 7

for i in range(base + 1, 0, -1):
    for j in range(i, 1, -1):
        print("*", end='')
    print()
