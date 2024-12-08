# N과 M (12)
from itertools import combinations_with_replacement
import sys

n, m = map(int, sys.stdin.readline().split())
numbers = sorted(map(int, sys.stdin.readline().split()))

for c in sorted(set(combinations_with_replacement(numbers, m))):
    print(*c)
