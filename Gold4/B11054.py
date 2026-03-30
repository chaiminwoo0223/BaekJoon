# 가장 긴 바이토닉 부분 수열
import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + 1)

s = dp.copy()

for i in range(1, n):
    for j in range(i):
        if a[i] < a[j]:
            s[i] = max(s[i], s[j] + 1)

print(max(s))
