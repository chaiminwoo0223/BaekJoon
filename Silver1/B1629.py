# 곱셈
# 재귀
import sys

a, b, c = map(int, sys.stdin.readline().split())

def power(a, b):
    if b == 1:
        return a % c
    else:
        number = power(a, b//2)
        if b % 2 == 0:
            return number * number % c
        else:
            return number * number * a % c

print(power(a, b))
