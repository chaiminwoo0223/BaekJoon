# 이친수
# 직접 구하는 것이 아니다.
import sys

n = int(sys.stdin.readline())
dp = [0] * (n+1) # 1차원 배열
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-2] + dp[i-1]
print(dp[n])
