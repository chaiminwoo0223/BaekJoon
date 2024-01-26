# 2×n 타일링
import sys

n = int(sys.stdin.readline())
cnt = [0] * (n+1) # 핵심

cnt[1] = 1
if n > 1:
    cnt[2] = 2
for i in range(3, n+1):
    cnt[i] = (cnt[i-1] + cnt[i-2]) % 10007

print(cnt[n])