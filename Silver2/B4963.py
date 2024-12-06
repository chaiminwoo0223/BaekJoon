# 섬의 개수
import sys
sys.setrecursionlimit(5000)

def dfs(x, y):
    visited[x][y] = 1

    # 8방향 탐색
    for i in range(8):
        nx = x + dh[i]
        ny = y + dw[i]

        # 지도 범위 내에 있고, 육지(1)이고, 방문하지 않았으면 탐색
        if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1 and visited[nx][ny] == 0:
            dfs(nx, ny)

while True:
    w, h = map(int, sys.stdin.readline().split())

    if w == 0 and h == 0:
        break
    else:
        dh = [-1, 0, 1, -1, 1, -1, 0, 1]
        dw = [-1, -1, -1, 0, 0, 1, 1, 1]
        graph = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
        visited = [[0] * w for _ in range(h)]
        count = 0

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and visited[i][j] == 0: # 새로운 섬 발견
                dfs(i, j)
                count += 1 # 섬 개수 증가
    
    print(count)
