# 영역 구하기
from collections import deque
import sys

def bfs():
    global area
    count = 0

    while q:
        x, y = q.popleft()
        graph[x][y] = 1
        count += 1
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < n and 0 <= ty < m and graph[tx][ty] == 0:
                graph[tx][ty] = 1
                q.append([tx, ty])

    result.append(count)
    area += 1

m, n, k = map(int, sys.stdin.readline().split())
graph = [[0] * m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
q = deque()
area = 0
result = []

for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            q.append([i, j])
            bfs()
            
print(area)           
print(*sorted(result))
