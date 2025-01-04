# 바이러스
from collections import deque
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)
q = deque()

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1

def bfs():
    while q:
        x = q.popleft()
        visited[x] = 1
        for y in range(1, n+1):
            if graph[x][y] == 1 and visited[y] == 0:
                q.append(y)

q.append(1)
visited[1] = 1
bfs()

print(sum(visited)-1)
