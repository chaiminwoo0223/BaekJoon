# 가장 큰 증가하는 부분 수열
# dp[i]를 초기화할 때, 자기 자신의 값(a[i])을 고려해야 한다.
import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = a.copy() # 핵심

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j]+a[i])

print(max(dp))
