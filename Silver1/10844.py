# 쉬운 계단 수
import sys

input = sys.stdin.readline

n = int(input())
x = [[0] * 10 for _ in range(n)]
x[0] = [0] + [1] * 9

# 점화식
for i in range(1, n):
    x[i][0] = x[i-1][1] # 끝자리 0
    x[i][9] = x[i-1][8] # 끝자리 9

    for j in range(1, 9): # 끝자리 1 ~ 8
        x[i][j] = x[i-1][j-1] + x[i-1][j+1]

print(sum(x[n-1]) % 1000000000)
