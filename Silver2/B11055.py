# 가장 큰 증가하는 부분 수열
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
numbers = a[:] # 초기화

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            numbers[i] = max(numbers[i], a[i]+numbers[j]) # 핵심

print(max(numbers))
