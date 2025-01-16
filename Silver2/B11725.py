# 트리의 부모 찾기
from collections import deque
import sys

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)] # 핵심
visited = [0] * (n+1)
q = deque()

for i in range(n-1):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs():
    while q:
        x = q.popleft()

        for next in graph[x]:
            if visited[next] == 0:
                q.append(next)
                visited[next] = x

q.append(1)
bfs()

for i in range(2, n+1):
    print(visited[i])
