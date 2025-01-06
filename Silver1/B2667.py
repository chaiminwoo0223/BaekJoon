# 단지번호붙이기
# list(map(int, sys.stdin.readline().rstrip())) -> 1101010 -> [1, 1, 0, 1, 0, 1, 0]
from collections import deque
import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = []
q = deque()

def bfs():
    count = 0

    while q:
        x, y = q.popleft()
        graph[x][y] = 1
        visited[x][y] = 1
        count += 1
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < n and 0 <= ty < n and graph[tx][ty] == 1 and visited[tx][ty] == 0:
                graph[tx][ty] = 1
                visited[tx][ty] = 1
                q.append([tx, ty])

    result.append(count)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            q.append([i, j])
            bfs()

print(len(result))
for r in sorted(result):
    print(r)
