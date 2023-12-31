# 공 넣기
import sys

n, m = map(int, sys.stdin.readline().split())
basket = [0 for _ in range(n)]

for _ in range(m):
    i, j, k = map(int, sys.stdin.readline().split())
    for l in range(i, j+1):
        basket[l-1] = k # 공의 번호
print(' '.join(str(e) for e in basket))