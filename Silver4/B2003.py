# 수들의 합 2
# 투 포인터(뱀 같음)
# O(n)
import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
start = 0
number = 0
count = 0

for end in range(n):
    number += a[end]

    while number > m:
        number -= a[start]
        start += 1

    if number == m:
        count += 1

print(count)
