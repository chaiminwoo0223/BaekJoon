# N과 M (7)
from itertools import product
import sys

n, m = map(int, sys.stdin.readline().split())
numbers = sorted(map(int, sys.stdin.readline().split()))

for p in product(numbers, repeat=m):
    print(*p)
