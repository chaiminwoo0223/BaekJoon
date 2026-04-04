# 가장 긴 증가하는 부분 수열 4
import sys

input = sys.stdin.readline

n = int(input())
a = [0] + list(map(int, input().split()))
dp = [[] for _ in range(n+1)]

for i in range(1, n+1):
    dp[i] = [a[i]]

for i in range(1, n+1):
    for j in range(1, i+1):
        if a[i] > a[j] and len(dp[j]) + 1 > len(dp[i]):
            dp[i] = dp[j] + [a[i]]

num = sorted(dp[1:], key=lambda x : len(x), reverse=True)

print(len(num[0]))
print(*num[0])
