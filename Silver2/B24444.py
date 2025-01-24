# 알고리즘 수업 - 너비 우선 탐색 1
from collections import deque
import sys

n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
q = deque(([r]))
count = 1

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs():
    global count

    while q:
        x = q.popleft()

        for next in sorted(graph[x]):
            if visited[next] == 0:
                q.append(next)
                count += 1
                visited[next] = count

visited[r] = 1
bfs()

for i in range(1, n+1):
    print(visited[i])
