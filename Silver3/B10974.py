# 모든 순열
from itertools import permutations
import sys

n = int(sys.stdin.readline())
numbers = list(range(1, n+1))
result = permutations(numbers, n)

for r in result:
    print(*r)
