# 연속합
import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
dp = [0] * n

dp[0] = numbers[0]
for i in range(1, len(numbers)):
    dp[i] = max(numbers[i], dp[i-1] + numbers[i])

print(max(dp))
