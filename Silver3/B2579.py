# 계단 오르기
# 동적 프로그래밍: Bottom-Up 방식
import sys

n = int(sys.stdin.readline())
stairs = [0] + [int(sys.stdin.readline()) for _ in range(n)]

if n < 2:
    print(stairs[n])
else:
    dp = [0] * (n+1) 
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]
    for i in range(3, n+1):
        dp[i] = max(dp[i-2], dp[i-3]+stairs[i-1]) + stairs[i] # 점화식
    print(dp[n])
