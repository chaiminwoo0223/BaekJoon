# 구간 합 구하기 4
import sys

n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
dp = [0] * (n+1) # 핵심

# 누적합
for i in range(1, n+1):
    dp[i] = dp[i-1] + numbers[i-1]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(dp[j] - dp[i-1])
