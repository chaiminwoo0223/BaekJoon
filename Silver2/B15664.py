# N과 M (10)
from itertools import combinations
import sys

n, m = map(int, sys.stdin.readline().split())
numbers = sorted(map(int, sys.stdin.readline().split()))

for c in sorted(set(combinations(numbers, m))):
    print(*c)
