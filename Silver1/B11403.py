# 경로 찾기
# 플로이드 워샬
# 한 정점에서 갈 수 있는 모든 정점을 검토
import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [0] * n

def dfs(x):
    for i in range(n):
        if graph[x][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)

for i in range(n):
    dfs(i)
    for j in range(n):
        if visited[j] == 1:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
    visited = [0] * n # 초기화
