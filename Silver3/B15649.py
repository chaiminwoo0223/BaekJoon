# N과 M (1)
from itertools import permutations
import sys

n, m = map(int, sys.stdin.readline().split())
numbers = list(range(1, n+1))

for permutation in permutations(numbers, m):
    print(" ".join(map(str, permutation))) # 튜플 -> 문자열 리스트 -> 리스트 문자열을 공백으로 연결
