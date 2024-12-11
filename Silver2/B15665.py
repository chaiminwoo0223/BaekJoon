# N과 M (11)
from itertools import product
import sys

n, m = map(int, sys.stdin.readline().split())
numbers = sorted(map(int, sys.stdin.readline().split()))

for p in sorted(set(product(numbers, repeat=m))):
    print(*p)
