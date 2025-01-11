# 연결 요소의 개수
from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)
q = deque()
count = 0

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u][v] = 1
    graph[v][u] = 1

def bfs():
    while q:
        x = q.popleft()
        for next in range(1, n+1):
            if graph[x][next] == 1 and visited[next] == 0:
                q.append(next)
                visited[next] = 1
                
for i in range(1, n+1):
    if visited[i] == 0:
        q.append(i)
        visited[i] = 1
        bfs()
        count += 1

print(count)
