# 정수 삼각형
import sys

n = int(sys.stdin.readline())
triangle = []

for i in range(n):
    triangle.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 위에서 아래로
for i in range(1, n):
    for j in range(len(triangle[i])):
        if j == 0:
            triangle[i][j] += triangle[i-1][j]
        elif j == (len(triangle[i])-1):
            triangle[i][j] += triangle[i-1][-1]
        else:
            triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])

print(max(triangle[-1]))
