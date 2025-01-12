# 헌내기는 친구가 필요해
from collections import deque
import sys

m, n = map(int, sys.stdin.readline().split())
q = deque()
campus = [list(sys.stdin.readline().rstrip()) for _ in range(m)]
visited = [[0] * n for _ in range(m)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(m):
    for j in range(n):
        if campus[i][j] == 'I':
            q.append([i, j])
            visited[i][j] = 1
            break

def bfs():
    count = 0

    while q:
        x, y = q.popleft()

        if campus[x][y] == 'P':
            count += 1

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if 0 <= tx < m and 0 <= ty < n and campus[tx][ty] != 'X' and visited[tx][ty] == 0:
                q.append([tx, ty])
                visited[tx][ty] = 1
    
    if count != 0:
        return count
    else:
        return "TT"

print(bfs())
