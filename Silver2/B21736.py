# 헌내기는 친구가 필요해
from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)] # 핵심
visited = [[0] * m for _ in range(n)] # 핵심2
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    count = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if 0 <= tx < n and 0 <= ty < m and graph[tx][ty] != 'X' and visited[tx][ty] == 0:
                if graph[tx][ty] == 'P':
                    count += 1
                visited[tx][ty] = 1
                q.append([tx, ty])

    return count

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            result = bfs(i, j)
            break

if result > 0:
    print(result)
else:
    print("TT")
