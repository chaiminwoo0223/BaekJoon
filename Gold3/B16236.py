# 아기 상어
# 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
# 가장 처음에 아기 상어의 크기는 2이고, 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동한다.
# 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
# 아기 상어의 이동은 1초 걸리고, 물고기를 먹는데 걸리는 시간은 없다.
# 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다.
from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
queue = deque()

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
cnt = 0
result = 0
x, y, size = 0, 0, 2

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x, y = i, j

def bfs(i, j, size):
    distance = [[0] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    queue.append((i, j))
    result = []

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if 0 <= tx < n and 0 <= ty < n and not visited[tx][ty]:
                if graph[tx][ty] <= size:
                    queue.append((tx, ty))
                    visited[tx][ty] = 1
                    distance[tx][ty] = distance[x][y] + 1

                    if graph[tx][ty] < size and graph[tx][ty]:
                        result.append((tx, ty, distance[tx][ty]))

    return sorted(result, key=lambda x: (-x[2], -x[0], -x[1]))

while True:
    shark = bfs(x, y, size)

    if len(shark) == 0:
        break

    tx, ty, distance = shark.pop()
    result += distance
    graph[x][y], graph[tx][ty] = 0, 0
    x, y = tx, ty
    cnt += 1

    if cnt == size:
        size += 1
        cnt = 0

print(result)
