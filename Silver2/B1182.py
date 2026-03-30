# 부분수열의 합
from itertools import combinations
import sys

input = sys.stdin.readline

n, s = map(int, input().split())
x = list(map(int, input().split()))
cnt = 0

for i in range(n):
    for c in combinations(x, i+1):
        if sum(c) == s:
            cnt += 1

print(cnt)
