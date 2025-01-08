# 미로 탐색 
from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
q = deque()

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < n and 0 <= ty < m and graph[tx][ty] == 1:
                q.append([tx, ty])
                graph[tx][ty] = graph[x][y] + 1

q.append([0, 0])
bfs()
print(graph[n-1][m-1])
