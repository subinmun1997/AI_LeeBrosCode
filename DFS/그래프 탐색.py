n, m = tuple(map(int, input().split()))

# index를 1번 부터 사용하기 위해 n+1만큼 할당합니다.
graph = [
    [0 for _ in range(n + 1)]
    for _ in range(n + 1)
]

visited = [False for _ in range(n + 1)]
vertex_cnt = 0


def dfs(vertex):
    global vertex_cnt
    global visited

    # 해당 정점에서 이어져있는 모든 정점을 탐색해줍니다.
    for curr_v in range(1, n + 1):
        # 아직 간선이 존재하고 방문한 적이 없는 정점에 대해서만 탐색을 진행합니다.
        if graph[vertex][curr_v] and not visited[curr_v]:
            visited[curr_v] = True
            vertex_cnt += 1
            dfs(curr_v)


for i in range(m):
    v1, v2 = tuple(map(int, input().split()))

    # 각 정점이 서로 이동이 가능한 양방향 그래프이기 때문에
    # 각 정점에 대한 간선을 각각 저장해줍니다.
    graph[v1][v2] = 1
    graph[v2][v1] = 1

visited[1] = True
dfs(1)

print(vertex_cnt)