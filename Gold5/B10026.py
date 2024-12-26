# 적록색약
from collections import deque
import sys

n = int(sys.stdin.readline())
graph = [[] for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
q = deque()
result = []

for i in range(n):
    for c in sys.stdin.readline().rstrip():
        graph[i].append(c)

def color(blind):
    count = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                q.append([i, j])
                bfs(blind)
                count += 1
    result.append(count)

def bfs(blind):
    while q:
        x, y = q.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < n and 0 <= ty < n and visited[tx][ty] == 0:
                if blind == True:
                    if graph[tx][ty] == graph[x][y] or (graph[tx][ty] == 'R' and graph[x][y] == 'G') or (graph[tx][ty] == 'G' and graph[x][y] == 'R'):
                        visited[tx][ty] = 1
                        q.append([tx, ty])
                else:
                    if graph[tx][ty] == graph[x][y]:
                        visited[tx][ty] = 1
                        q.append([tx, ty])


visited = [[0] * n for _ in range(n)]
color(False) # 적록색약 X
visited = [[0] * n for _ in range(n)]
color(True) # 적록색약 O

print(*result)
