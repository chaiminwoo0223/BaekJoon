# 케빈 베이컨의 6단계 법칙
# bfs
from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[0] * (n+1) for _ in range(n+1)]
count = 0
result = []

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

def bfs(v):
    q = deque()
    q.append(v)
    while q:
        current = q.popleft()
        for next in range(1, n+1):
            if not visited[next] and graph[current][next]:
                visited[next] = visited[current] + 1
                q.append(next)

for i in range(1, n+1):
    visited = [0] * (n+1)
    bfs(i)
    visited[i] = 0 # 자기자신 제외
    result.append(sum(visited))

print(result.index(min(result)) + 1)
