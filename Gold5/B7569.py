# 토마토 2
from collections import deque
import sys

m, n, h = map(int, sys.stdin.readline().split())
graph = [list(list(map(int, sys.stdin.readline().split())) for _ in range(n)) for _ in range(h)]
dt = [[-1, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1], [0, -1, 0], [0, 0, -1]]
q = deque()
count = 0

def bfs():
    while q:
        x, y, z = q.popleft()

        for i in range(6):
            tx = x + dt[i][0]
            ty = y + dt[i][1]
            tz = z + dt[i][2]

            if 0 <= tx < h and 0 <= ty < n and 0 <= tz < m and graph[tx][ty][tz] == 0:
                graph[tx][ty][tz] = graph[x][y][z] + 1
                q.append([tx, ty, tz])

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append([i, j, k])

bfs()

for i in range(h):
    for j in range(n):
        if 0 in graph[i][j]:
            print(-1)
            sys.exit()
        else:
            count = max(count, max(graph[i][j]))

print(count - 1)
