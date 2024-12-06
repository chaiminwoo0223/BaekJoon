# 제곱수의 합
# 점화식
import sys
import math

n = int(sys.stdin.readline())
dp = [x for x in range(n+1)]

for i in range(1, n+1):
    for j in range(1, int(math.sqrt(i))+1):
        dp[i] = min(dp[i], dp[i-j**2]+1)

print(dp[n])
