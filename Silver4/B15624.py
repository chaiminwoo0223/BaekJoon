# 피보나치 수 7
import sys

n = int(sys.stdin.readline())

if n == 0:
    print(0)
else:
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, (a + b) % 1000000007
    print(b)
