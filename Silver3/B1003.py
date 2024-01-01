# 피보나치 함수
import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    zero, one = 1, 0 # 핵심1
    for j in range(n):
        zero, one = one, zero + one # 피보나치(핵심2)
    print(zero, one)