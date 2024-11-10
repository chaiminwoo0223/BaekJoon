# N과 M (5)
from itertools import permutations
import sys

n, m = map(int, sys.stdin.readline().split())
numbers = sorted(map(int, sys.stdin.readline().split()))

for p in permutations(numbers, m):
    print(" ".join(map(str, p)))
