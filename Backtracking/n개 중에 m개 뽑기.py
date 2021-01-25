# 변수 선언 및 입력

n, m = tuple(map(int, input().split()))
visited = [
    False for _ in range(n + 1)
]


# 방문한 원소들을 출력해줍니다.
def print_combination():
    for i in range(1, n + 1):
        if visited[i]:
            print(i, end=" ")

    print()


# 지금까지 뽑은 갯수와 마지막으로 뽑힌 숫자를 추적하여
# 그 다음에 뽑힐 수 있는 원소의 후보를 정합니다.
def find_combination(cnt, last_num):
    # m개를 모두 뽑은 경우 답을 출력해줍니다.
    if cnt == m:
        print_combination()
        return

    # 뽑을 수 있는 원소의 후보들을 탐색합니다.
    for i in range(last_num + 1, n + 1):
        visited[i] = True;
        find_combination(cnt + 1, i);
        visited[i] = False;


# 가능한 범위를 순회하며 해당 숫자가
# 조합의 첫번째 숫자일 때를 탐색합니다.
for i in range(1, n + 1):
    visited[i] = True
    find_combination(1, i)
    visited[i] = False