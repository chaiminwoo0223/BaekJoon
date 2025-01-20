# 연구소
# 벽을 적절한 위치에 배치해야 한다.
from collections import deque
from itertools import combinations
from copy import deepcopy
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
blank = []
virus = []
maximum = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0: # 0: 빈 칸
            blank.append([i, j])
        if graph[i][j] == 2: # 2: 바이러스
            virus.append([i, j])

# 확산
def bfs():
    q = deque(virus)

    while q:
        x, y = q.popleft()

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if 0 <= tx < n and 0 <= ty < m and vgraph[tx][ty] == 0:
                vgraph[tx][ty] = 2
                q.append([tx, ty])
    
# 벽 + 빈칸
for combination in combinations(blank, 3):
    vgraph = deepcopy(graph)
    count = 0

    for x, y in combination:
        vgraph[x][y] = 1

    bfs()

    for i in range(n):
        for j in range(m):
            if vgraph[i][j] == 0:
                count += 1
    
    maximum = max(maximum, count)

print(maximum)
