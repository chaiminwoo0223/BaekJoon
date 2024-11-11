# 단지번호붙이기
from collections import deque
import sys

def bfs(x, y):
    count = 1
    graph[x][y] = 0 # 탐색 중인 위치 0으로 바꿔 다시 방문하지 않도록 함
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                count += 1
                graph[nx][ny] = 0
                q.append((nx, ny))
    return count

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
result = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
q = deque()

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(bfs(i, j))

print(len(result))
for r in sorted(result):
    print(r)
