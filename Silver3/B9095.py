# 1, 2, 3 더하기
# 다이나믹 프로그래밍 => 점화식 => 손
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    cnt = [0] * (n+1)
    for i in range(1,n+1):
        if i == 1:
            cnt[i] = 1
        elif i == 2:
            cnt[2] = 2
        elif i == 3:
            cnt[3] = 4
        else:
            cnt[i] = cnt[i-1] + cnt[i-2] + cnt[i-3]
    print(cnt[n])