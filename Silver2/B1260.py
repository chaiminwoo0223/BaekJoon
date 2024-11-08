# DFS와 BFS
# 큐 <<< 덱
from collections import deque
import sys

def dfs(v):
    visited[v] = True
    print(v, end=" ")
    for next in range(1, n+1):
        if not visited[next] and graph[v][next]:
            dfs(next)

def bfs():
    while q:
        current = q.popleft()
        print(current, end=" ")
        for next in range(1, n+1):
            if not visited[next] and graph[current][next]:
                visited[next] = True
                q.append(next)

n, m, v = map(int, sys.stdin.readline().split())
graph = [[False] * (n+1) for _ in range(n+1)] # 핵심
visited = [False] * (n+1) # 핵심
q = deque()

# 그래프 초기화
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = True
    graph[b][a] = True

# DFS
dfs(v)
print()

# BFS
visited = [False] * (n+1) # 핵심
q.append(v)
visited[v] = True
bfs()
