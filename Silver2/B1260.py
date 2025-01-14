# DFS와 BFS
from collections import deque
import sys

n, m, v = map(int, sys.stdin.readline().split())
graph = [[0] * (n+1) for _ in range(n+1)]
q = deque()

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1

def dfs(x):
    print(x, end=' ')

    for next in range(1, n+1):
        if graph[x][next] == 1 and visited[next] == 0:
            visited[next] = 1
            dfs(next)

def bfs():
    while q:
        x = q.popleft()
        print(x, end=' ')

        for next in range(1, n+1):
            if graph[x][next] == 1 and visited[next] == 0:
                q.append(next)
                visited[next] = 1

# dfs
visited = [0] * (n+1)
visited[v] = 1
dfs(v)
print()

# bfs
visited = [0] * (n+1)
q.append(v)
visited[v] = 1
bfs()
