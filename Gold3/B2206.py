# 벽 부수고 이동하기
# 만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.
# 한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.
# BFS는 가장 먼저 목적지에 도달하는 경로가 곧 최단 거리임을 보장한다.
# 벽을 이미 부수고 온 경로 vs 아직 부수지 않고 온 경로
# visited[n][m][2] 형태의 3차원 배열
from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[int(x) for x in input().rstrip()] for _ in range(n)]

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)] # 핵심

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

queue = deque()

def bfs():
    while queue:
        x, y, crashed = queue.popleft()

        if x == n - 1 and y == m - 1:
            return visited[x][y][crashed]

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if 0 <= tx < n and 0 <= ty < m:
                if not graph[tx][ty] and not visited[tx][ty][crashed]: # 이동할 곳이 빈칸(0)이고, 아직 방문하지 않음
                    visited[tx][ty][crashed] = visited[x][y][crashed] + 1
                    queue.append((tx, ty, crashed))

                if graph[tx][ty] and (not crashed and not visited[tx][ty][1]): # 이동할 곳이 벽(1)이고, 아직 벽을 부수지 않음
                    visited[tx][ty][1] = visited[x][y][0] + 1
                    queue.append((tx, ty, 1))

    return -1

queue.append((0, 0, 0))
visited[0][0][0] = 1

print(bfs())
