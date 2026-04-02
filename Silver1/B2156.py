# 포도주 시식
# 잔을 안 마시는 경우 -> [100, 100, 1, 1, 100, 100]
import sys

input = sys.stdin.readline

n = int(input())
wines = [int(input()) for _ in range(n)]
dp = [0] * (n+1)
dp[1] = wines[0]

if n >= 2:
    dp[2] = wines[0] + wines[1]

for i in range(3, n+1):
    dp[i] = max(dp[i-1], dp[i-2] + wines[i-1], dp[i-3] + wines[i-2] + wines[i-1])

print(max(dp))

