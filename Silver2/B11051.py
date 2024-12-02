# 이항 계수 2
import math
import sys

n, k = map(int, sys.stdin.readline().split())
pascal = [[1] * (i+1) for i in range(n+1)]

# 파스칼 삼각형(DP)
for i in range(2, n+1):
    for j in range(1, i):
        pascal[i][j] = (pascal[i-1][j-1] + pascal[i-1][j]) % 10007

print(pascal[n][k])
