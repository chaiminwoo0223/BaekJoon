# LCS
# dp 테이블
import sys

lcs1 = sys.stdin.readline().rstrip()
lcs2 = sys.stdin.readline().rstrip()
n = len(lcs1)
m = len(lcs2)
dp = [[0] * (m+1) for _ in range(n+1)] # dp 테이블 초기화

for i in range(1, n+1):
    for j in range(1, m+1):
        if lcs1[i-1] == lcs2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[n][m])
