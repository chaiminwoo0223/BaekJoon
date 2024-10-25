# 퇴사
import sys

n = int(sys.stdin.readline())
consultations = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
dp = [0] * (n+1) # DP 테이블 초기화

for i in range(n):
    t, p = consultations[i]
    if i + t <= n:
        dp[i+t] = max(dp[i+t], dp[i]+p)
    dp[i+1] = max(dp[i+1], dp[i])

print(dp[n])
