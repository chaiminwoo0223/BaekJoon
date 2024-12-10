# N과 M (6)
from itertools import combinations
import sys

n, m = map(int, sys.stdin.readline().split())
numbers = sorted(map(int, sys.stdin.readline().split()))

for c in combinations(numbers, m):
    print(*c)
