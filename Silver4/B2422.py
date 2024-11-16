# 한윤정이 이탈리아에 가서 아이스크림을 사먹는데
# 2차원 리스트
from itertools import combinations
import sys

n, m = map(int, sys.stdin.readline().split())
combination = combinations(list(range(1, n+1)), 3)
t = [[False] * (n+1) for _ in range(n+1)]
count = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    t[a][b] = True
    t[b][a] = True

for c in combination:
    i, j, k = c
    if not t[i][j] and not t[j][k] and not t[i][k]:
        count += 1

print(count)
