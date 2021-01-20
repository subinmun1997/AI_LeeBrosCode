n = int(input())
members = list(map(int, input().split()))

min = members[0]
sum = 0

for i in range(1, n):
    if min > members[i]:
        min = members[i]

for i in range(n):
    if members[i] == min:
        sum += 1

print(min, sum)