# 카잉 달력
import sys

def solution(m, n, x, y):
    k = x
    while k <= m * n:
        if (k - x) % m == 0 and (k - y) % n == 0:
            return k
        k += m
    return -1


t = int(sys.stdin.readline())

for _ in range(t):
    m, n, x, y = map(int, sys.stdin.readline().split())
    print(solution(m, n, x, y))
