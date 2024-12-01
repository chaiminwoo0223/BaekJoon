# 수들의 합 2
# 투 포인터
# O(n)
import sys

n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
result = 0
count = 0
start = 0

for end in range(n):
    result += numbers[end]

    while result > m:
        result -= numbers[start]
        start += 1

    if result == m:
        count += 1

print(count)
