# 대지
import sys

n = int(sys.stdin.readline().strip())
X = []
Y = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    X.append(x)
    Y.append(y)

if len(X) == 1 or len(Y) == 1:
    print(0)
else:
    land = (max(X)-min(X)) * (max(Y)-min(Y))
    print(land)
