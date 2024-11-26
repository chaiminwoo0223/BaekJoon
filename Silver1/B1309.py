# 동물원
# 점화식
import sys

n = int(sys.stdin.readline())
dp = [1, 3]

for _ in range(2, n+1):
    result = 2 * dp[1] + dp[0]
    dp[0] = dp[1]
    dp[1] = result

print(dp[1] % 9901)
