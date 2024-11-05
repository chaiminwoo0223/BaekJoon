# 백설 공주와 일곱 난쟁이
from itertools import combinations
import sys

dwarfs = []
result = 0

for _ in range(9):
    dwarfs.append(int(sys.stdin.readline()))

for combination in combinations(dwarfs, 7):
    if sum(combination) == 100:
        result = combination
        break

for r in result:
    print(r)
