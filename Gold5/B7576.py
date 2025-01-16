# 토마토
from collections import deque
import sys

m, n = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
q = deque()
tomato = True
count = 0

def bfs():
    global count
    while q:
        x, y = q.popleft()

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if 0 <= tx < n and 0 <= ty < m and graph[tx][ty] == 0:
                graph[tx][ty] = graph[x][y] + 1
                q.append([tx, ty])

# 저장될 때부터 모든 토마토가 익어있다면
for i in range(n):
    if 0 in graph[i]:
        tomato = False
        break

if tomato:
    print(0)
    sys.exit()

# bfs
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append([i, j])

bfs()

# 익지 않은 토마토가 있다면
for i in range(n):
    if 0 in graph[i]:
        count = 0
        break
    else:
        count = max(count, max(graph[i]))

print(count - 1)
