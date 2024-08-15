# 알고리즘 수업 - 점근적 표기 1
import sys

a1, a0 = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())
n = int(sys.stdin.readline())

if ((a1*n + a0) <= c*n) and a1 <= c:
    print(1)
else:
    print(0)
    