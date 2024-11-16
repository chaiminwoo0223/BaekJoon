# Four Squares
# PyPy3
import sys

n = int(sys.stdin.readline())
dp = [0, 1]

for i in range(2, n+1):
    target = 1e9
    for j in range(1, 50001):
        if j**2 > i:
            break
        target = min(target, dp[i-j**2]) # 제곱수들의 최소 개수
    dp.append(target+1)
print(dp[n])
