# 가장 긴 증가하는 부분 수열
import sys

a = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [1] * a

for i in range(1, a):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
