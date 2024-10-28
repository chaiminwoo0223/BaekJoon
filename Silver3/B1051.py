# 숫자 정사각형
# 삼중 for 문
import sys

n, m = map(int, sys.stdin.readline().split())
size = min(n, m)
dice = []
area = 0

for _ in range(n):
    dice.append(list(sys.stdin.readline().rstrip()))

for i in range(n):
    for j in range(m):
        for k in range(size):
            if (i + k) < n and (j + k) < m and dice[i][j] == dice[i+k][j] == dice[i][j+k] == dice[i+k][j+k]:
                area = max(area, (k+1)**2)

print(area)
