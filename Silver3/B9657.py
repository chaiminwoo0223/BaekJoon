# 돌 게임 3
import sys

n = int(sys.stdin.readline())
dp = [False] * (n+1)

if n >= 1:
    dp[1] = True
if n >= 2:
    dp[2] = False
if n >= 3:
    dp[3] = True
if n >= 4:
    dp[4] = True

for i in range(5, n+1):
    dp[i] = not dp[i-1] or not dp[i-3] or not dp[i-4]

if dp[n]:
    print("SK")
else:
    print("CY")
