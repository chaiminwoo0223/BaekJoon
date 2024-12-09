# 곱셈
# 지수 법칙 + 나머지 분배 법칙
import sys

a, b, c = map(int, sys.stdin.readline().split())

def sol(a, b):
    if b == 1:
        return a % c
    else:
        number = sol(a, b//2)
        if b % 2 == 0:
            return number * number % c
        else:
            return number * number * a % c

print(sol(a, b))
