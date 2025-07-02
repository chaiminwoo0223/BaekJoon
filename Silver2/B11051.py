# 이항 계수 2
from math import comb

n, k = map(int, input().split())

print(comb(n, k) % 10007)
