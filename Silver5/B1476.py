# 날짜 계산
import sys

e, s, m = map(int, sys.stdin.readline().split())
x, y, z = 0, 0, 0
year = 0

while x != e or y != s or z != m:
    year += 1
    x = x % 15 + 1
    y = y % 28 + 1
    z = z % 19 + 1

print(year)
