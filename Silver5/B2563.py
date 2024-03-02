# 색종이
from sys import stdin

n = int(stdin.readline())
arr = [[0] * 101 for _ in range(101)]

for _ in range(n):
    a, b = map(int, stdin.readline().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            arr[i][j] = 1

print(sum(sum(row) for row in arr))