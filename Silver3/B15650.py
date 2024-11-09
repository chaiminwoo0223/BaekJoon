# N과 M (2)
from itertools import combinations
import sys

n, m = map(int, sys.stdin.readline().split())
numbers = list(range(1, n+1))

for combination in combinations(numbers, m):
    print(" ".join(sorted(map(str, combination))))
