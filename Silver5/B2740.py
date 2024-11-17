# 행렬 곱셈
import sys

n, m = map(int, sys.stdin.readline().split())
matrix1 = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
m, k = map(int, sys.stdin.readline().split())
matrix2 = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
result = []

for a in range(n):
    for c in range(k):
        total = 0
        for b in range(m):
            total += matrix1[a][b] * matrix2[b][c]
        result.append(total)

for i in range(0, len(result), k):
    print(*result[i:i+k])
