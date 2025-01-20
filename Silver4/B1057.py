# 토너먼트
import sys

n, m, o = map(int, sys.stdin.readline().split())
count = 0

while m != o:
    m -= m // 2
    o -= o // 2
    count += 1

print(count)
