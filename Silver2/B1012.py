# 유기농 배추
from collections import deque
import sys

t = int(sys.stdin.readline())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
q = deque()

def bfs():
    while q:
        x, y = q.popleft()

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if 0 <= tx < m and 0 <= ty < n and graph[tx][ty] == 1:
                q.append([tx, ty])
                graph[tx][ty] = 0

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0] * n for _ in range(m)]
    count = 0

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[x][y] = 1

    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                q.append([i, j])
                graph[i][j] = 0
                bfs()
                count += 1

    print(count)
