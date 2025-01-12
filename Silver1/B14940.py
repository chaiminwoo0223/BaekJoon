# 쉬운 최단거리
from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            q.append([i, j])

def bfs():
    while q:
        x, y = q.popleft()

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if 0 <= tx < n and 0 <= ty < m and graph[tx][ty] == 1 and visited[tx][ty] == 0:
                q.append([tx, ty])
                visited[tx][ty] = visited[x][y] + 1

bfs()

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and graph[i][j] == 1:
            visited[i][j] = -1

for i in range(n):
    print(*visited[i])
