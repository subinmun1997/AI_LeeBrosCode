# 변수 선언 및 입력
n, t = tuple(map(int, input().split()))
u = list(map(int, input().split()))
d = list(map(int, input().split()))

for _ in range(t):
    # Step 1
    # 위에서 가장 오른쪽에 있는 숫자를 따로 temp값에 저장해놓습니다.
    temp = u[n - 1]

    # Step 2
    # 위에 있는 숫자들을 완성합니다.
    # 오른쪽에서부터 채워넣어야 하며,
    # 맨 왼쪽 숫자는 아래에서 가져와야함에 유의합니다.
    for i in range(n - 1, 0, -1):
        u[i] = u[i - 1]
    u[0] = d[n - 1]

    # Step 3
    # 아래에 있는 숫자들을 완성합니다.
    # 마찬가지로 오른쪽에서부터 채워넣어야 하며,
    # 맨 왼쪽 숫자는 위에서 미리 저장해놨던 temp값을 가져와야함에 유의합니다.
    for i in range(n - 1, 0, -1):
        d[i] = d[i - 1]
    d[0] = temp

# 출력
for elem in u:
    print(elem, end=" ")
print()

for elem in d:
    print(elem, end=" ")