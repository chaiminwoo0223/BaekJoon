# 수들의 합
import sys

s = int(sys.stdin.readline())
result = 0
count = 0

while True:
    count += 1
    result += count

    if result > s:
        break

print(count-1)
