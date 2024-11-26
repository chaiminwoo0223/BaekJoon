# 2차원 배열의 합
# 다이나믹 프로그래밍
import sys

n, m = map(int, sys.stdin.readline().split())
numbers = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
k = int(sys.stdin.readline())
dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = numbers[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] # 누적합(중복 제거)

for _ in range(k):
    i, j, x, y = map(int, sys.stdin.readline().split())
    result = dp[x][y] - dp[i-1][y] - dp[x][j-1] + dp[i-1][j-1] # 구간 (i, j)부터 (x, y)까지의 합
    print(result)
