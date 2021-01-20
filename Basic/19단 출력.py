n = 20
for i in range(1, n):
    for j in range(1, n):
        if j % 2 == 0:
            print('/', i, '*', j, '=', i * j)
        else:
            print(i, '*', j, '=', i * j, end=' ')

    if j == 19:
        print()