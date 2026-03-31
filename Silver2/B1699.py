# 제곱수의 합
import sys

input = sys.stdin.readline

n = int(input())
dp = [x for x in range(n+1)] # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 -> 1^2 개수

for i in range(1, n+1):
    for j in range(1, i):
        if j**2 > i:
            break

        if dp[i] > dp[i - j**2] + 1: # 핵심
            dp[i] = dp[i - j**2] + 1

print(dp[n])
