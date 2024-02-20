# 행렬 덧셈
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

matrix1 = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
matrix2 = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
result_matrix = [[matrix1[i][j] + matrix2[i][j] for j in range(m)] for i in range(n)]

for row in result_matrix:
    print(' '.join(map(str, row)))