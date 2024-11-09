# 로또
from itertools import combinations
import sys

while True:
    lotto = list(map(int, sys.stdin.readline().split()))
    k = lotto[0]
    s = lotto[1:]
    if k != 0:
        for combination in combinations(s, 6):
            print(" ".join(map(str, combination)))
    else:
        break
    print()
