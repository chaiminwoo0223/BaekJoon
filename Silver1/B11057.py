# 오르막 수
# 대각선 합
import sys

n = int(sys.stdin.readline())
dp = [[0] * 10 for _ in range(n+1)]

# 첫 행은 모두 1
for i in range(10):
    dp[1][i] = 1

# 점화식
for i in range(2, n+1):
    for j in range(10):
        if j > 0:
            dp[i][j] = dp[i][j-1]+ dp[i-1][j]
        else:
            dp[i][j] = 1 # 첫 열은 모두 1

print(sum(dp[n]) % 10007)
