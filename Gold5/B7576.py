# 토마토
from collections import deque
import sys

m, n = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
q = deque()
count = 1

# 익은 토마토의 위치를 큐에 삽입
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append([i, j])

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if 0 <= tx < n and 0 <= ty < m and graph[tx][ty] == 0:
                graph[tx][ty] = graph[x][y] + 1 # 상하좌우에 익지 않은 토마토가 있으면 1을 더함
                q.append([tx, ty])
                
bfs()

for i in range(n):
    if 0 in graph[i]:
        count = 0
        break
    count = max(count, max(graph[i]))

print(count - 1)
