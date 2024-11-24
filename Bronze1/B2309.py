# 일곱 난쟁이
from itertools import combinations
import sys

dwarfs = [int(sys.stdin.readline()) for _ in range(9)]
combination = combinations(dwarfs, 7)
result = 0

for c in combination:
    if sum(c) == 100:
        result = sorted(c)
        break

for r in result:
    print(r)
