# N과 M (4)
from itertools import combinations_with_replacement
import sys

n, m = map(int, sys.stdin.readline().split())
numbers = list(range(1, n+1))

for c in combinations_with_replacement(numbers, m):
    print(" ".join(map(str, c)))
