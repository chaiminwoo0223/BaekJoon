# N과 M (9)
from itertools import permutations
import sys

n, m = map(int, sys.stdin.readline().split())
numbers = sorted(map(int, sys.stdin.readline().split()))

for p in sorted(set(permutations(numbers, m))):
    print(*p)
