# 1, 2, 3 더하기 3
# 이미 계산된 값은 다시 계산하지 않는다.
import sys

t = int(sys.stdin.readline())
dp = [0, 1, 2, 4]
complete = 3

for _ in range(t):
    n = int(sys.stdin.readline())

    if n > complete:
        for i in range(complete+1, n+1):
            dp.append((dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009)
        complete = n # 핵심

    print(dp[n])
