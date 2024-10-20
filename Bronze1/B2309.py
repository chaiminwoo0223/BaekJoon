# 일곱 난쟁이
from itertools import combinations
import sys

dwarfs = []

for _ in range(9):
    dwarfs.append(int(sys.stdin.readline()))

for combination in combinations(dwarfs, 7):
    if sum(combination) == 100:
        dwarfs = combination
        break

for dwarf in sorted(dwarfs):
    print(dwarf)
