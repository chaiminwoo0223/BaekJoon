# 차이를 최대로
from itertools import permutations
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
numbers = permutations(a, n)
result = []

for number in numbers:
    d = 0
    for i in range(1, n):
        d += abs(number[i-1] - number[i])
    result.append(d)

print(max(result))
