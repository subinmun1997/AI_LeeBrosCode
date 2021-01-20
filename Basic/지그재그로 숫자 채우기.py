n, m = list(map(int, input().split()))

answer = [
    [0 for _ in range(m)]
    for _ in range(n)
]

count = 1
for col in range(m):
    if col % 2 == 0:
        for row in range(n):
            answer[row][col] = count
            count += 1
    else:
        for row in range(n - 1, -1, -1):
            answer[row][col] = count
            count += 1

for row in range(n):
    for col in range(m):
        print(answer[row][col], end=' ')
    print()
