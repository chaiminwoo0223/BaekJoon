# 쉬운 최단거리
# bfs
from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
graph = []
visited = [[0] * m for _ in range(n)]
result = [[-1] * m for _ in range(n)] # 핵심
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
q = deque()

for i in range(n):
    numbers = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        if numbers[j] == 2: # 핵심2
            q.append([i, j])
            visited[i][j] = 1
            result[i][j] = 0
    graph.append(numbers)

def bfs():
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < n and 0 <= ty < m and visited[tx][ty] == 0:
                visited[tx][ty] = 1
                if graph[tx][ty] != 0:
                    result[tx][ty] = result[x][y] + 1
                    q.append([tx, ty])

bfs()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0: # 핵심3
            result[i][j] = 0
    print(*result[i])
