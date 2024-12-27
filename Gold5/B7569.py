# 토마토2
from collections import deque
import sys

m, n, h = map(int, sys.stdin.readline().split())
box = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
dx = [0, 0, 0, 0, -1, 1]
dy = [0, 1, 0, -1, 0, 0]
dz = [-1, 0, 1, 0, 0, 0]
q = deque()
count = -1

for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                q.append([i, j, k])

def bfs():
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            tx = x + dx[i]
            ty = y + dy[i]
            tz = z + dz[i]
            if 0 <= tx < h and 0 <= ty < n and 0 <= tz < m and box[tx][ty][tz] == 0:
                box[tx][ty][tz] = box[x][y][z] + 1
                q.append([tx, ty, tz])

bfs()

for i in range(h):
    for j in range(n):
        if 0 in box[i][j]:
            count = 0
            break
        else:
            count = max(count, max(box[i][j]))
    if count == 0:
        break

print(count - 1)
