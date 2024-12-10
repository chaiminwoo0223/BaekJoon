# 가장 긴 감소하는 부분 수열
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
length = [1] * n

for i in range(1, n):
    for j in range(i):
        if a[i] < a[j]:
            length[i] = max(length[i], length[j]+1) # 핵심

print(max(length))
