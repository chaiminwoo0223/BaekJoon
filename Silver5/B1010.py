# 다리 놓기
# 조합: 순서를 고려하지 않고 선택
import sys
import math

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    print(math.comb(m, n))
    