# 이동하기
# 누적합
# 2차원 리스트 -> 깊은 복사
import copy
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = copy.deepcopy(graph)
dx = [1, 0, 1]
dy = [0, 1, 1]

def check(x, y):
    for i in range(3):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < n and 0 <= ty < m:
            dp[tx][ty] = max(dp[tx][ty], graph[tx][ty] + dp[x][y])

for i in range(n):
    for j in range(m):
        check(i, j)

print(dp[n-1][m-1])
