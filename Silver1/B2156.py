# 포도주 시식
# 잔을 안 마시는 경우 -> [100, 100, 1, 1, 100, 100]
import sys

input = sys.stdin.readline

n = int(input())
x = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n+1)

dp[1] = x[1]

if n > 1:
    dp[2] = x[1] + x[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-2] + x[i], dp[i-3] + x[i-1] + x[i], dp[i-1])

print(max(dp))
