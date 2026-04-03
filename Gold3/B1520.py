# 내리막 길
import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1

    if dp[x][y] == -1:
        dp[x][y] = 0

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if 0 <= tx < m and 0 <= ty < n and graph[x][y] > graph[tx][ty]:
                dp[x][y] += dfs(tx, ty) # 핵심

    return dp[x][y]

print(dfs(0, 0))
