# 케빈 베이컨의 6단계 법칙
from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
q = deque()
result = [0, 5000]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(w):
    global result

    while q:
        x, count = q.popleft()

        for next in graph[x]:
            if visited[next] == 0:
                q.append([next, count+1])
                visited[next] = visited[x] + 1

    if result[1] > sum(visited) - visited[w]:
        result = [w, sum(visited) - visited[w]]

for i in range(1, n+1):
    visited = [0] * (n+1)
    q.append([i, 0])
    bfs(i)

print(result[0])
