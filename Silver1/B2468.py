# 안전 영역
from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

graph = []
s = set()
queue = deque()

for _ in range(n):
    regions = list(map(int, input().split()))
    graph.append(regions)
    s.update(set(regions))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = []

def bfs():
    global cnt

    cnt += 1

    while queue:
        x, y = queue.popleft()

        for a in range(4):
            tx = x + dx[a]
            ty = y + dy[a]

            if 0 <= tx < n and 0 <= ty < n and graph[tx][ty] and not visited[tx][ty]:
                queue.append([tx, ty])
                visited[tx][ty] = 1

for num in range(max(s) + 1):
    cnt = 0
    visited = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] <= num:
                graph[i][j] = 0
                visited[i][j] = 1

    for i in range(n):
        for j in range(n):
            if graph[i][j] and not visited[i][j]:
                queue.append([i, j])
                bfs()

    result.append(cnt)

if result:
    print(max(result))
