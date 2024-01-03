# 수 정렬하기
import sys

arr = []
n = int(sys.stdin.readline())

for _ in range(n):
    arr.append(int(sys.stdin.readline()))

for i in sorted(arr):
    print(i)