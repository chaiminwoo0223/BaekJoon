# N과 M (7)
from itertools import combinations_with_replacement
import sys

n, m = map(int, sys.stdin.readline().split())
numbers = sorted(map(int, sys.stdin.readline().split()))

for c in combinations_with_replacement(numbers, m):
    print(*c)
