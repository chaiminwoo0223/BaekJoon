# 경로 찾기
# 한 정점에서 갈 수 있는 모든 정점을 검토
n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n

def dfs(x):
    for j in range(n):
        if graph[x][j] == 1 and visited[j] == 0:
            visited[j] = 1
            dfs(j)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[j] == 0:
            visited[j] = 1
            dfs(j)

    for k in range(n):
        print(visited[k], end=" ")
    print()

    visited = [0] * n # 초기화
