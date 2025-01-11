# 섬의 개수
from collections import deque
import sys

q = deque()
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def bfs():
    while q:
        x, y = q.popleft()

        for i in range(8):
            tx = x + dx[i]
            ty = y + dy[i]

            if 0 <= tx < h and 0 <= ty < w and graph[tx][ty] == 1 and visited[tx][ty] == 0:
                q.append([tx, ty])
                visited[tx][ty] = 1

while True:
    w, h = map(int, sys.stdin.readline().split())
    graph = []
    visited = [[0] * w for _ in range(h)]
    count = 0
    
    if w == 0 and h == 0:
        break
    else:
        for i in range(h):
            graph.append(list(map(int, sys.stdin.readline().split())))

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and visited[i][j] == 0:
                q.append([i, j])
                visited[i][j] = 1
                bfs()
                count += 1

    print(count)
