# 나이트의 이동
from collections import deque
import sys

t = int(sys.stdin.readline())
dx = [2, 2, 1, 1, -1, -1, -2, -2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]
q = deque()

def bfs():
    result = []
    while q:
        x, y, count = q.popleft()

        if x == u and y == v:
            result.append(count)
            graph[x][y] = 0
            
        for i in range(8):
            tx = x + dx[i]
            ty = y + dy[i]

            if 0 <= tx < n and 0 <= ty < n and graph[tx][ty] == 0:
                q.append([tx, ty, count+1])
                graph[tx][ty] = 1

    return min(result)
                
for _ in range(t):
    n = int(sys.stdin.readline())
    graph = [[0] * n for _ in range(n)]
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = 1
    u, v = map(int, sys.stdin.readline().split())
    q.append([x, y, 0])

    print(bfs())
