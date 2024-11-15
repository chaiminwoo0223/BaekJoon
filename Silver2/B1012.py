# 유기농 배추
from collections import deque
import sys

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny]: # 범위 설정
                q.append((nx, ny))
                graph[nx][ny] = False

t = int(sys.stdin.readline())
q = deque()
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[False] * n for _ in range(m)] # 핵심
    count = 0

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[x][y] = True
        
    for i in range(m):
        for j in range(n):
            if graph[i][j]:
                q.append((i, j))
                graph[i][j] = False
                bfs()
                count += 1
    
    print(count)
