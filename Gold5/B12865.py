# 평범한 배낭
# 나눌 수 없음
# 다이나믹 프로그래밍
# 메모이제이션
import sys

n, k = map(int, sys.stdin.readline().split())
things = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        if j >= things[i-1][0]: # 현재 물건을 담을 수 있는 경우
            dp[i][j] = max(dp[i-1][j], things[i-1][1] + dp[i-1][j-things[i-1][0]])
        else: # 현재 물건을 담을 수 없는 경우
            dp[i][j] = dp[i-1][j]

print(dp[n][k])
