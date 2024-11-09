# N과 M (3)
from itertools import product
import sys

n, m = map(int, sys.stdin.readline().split())
numbers = list(range(1, n+1))

for p in product(numbers, repeat=m):
    print(" ".join(map(str, p)))
