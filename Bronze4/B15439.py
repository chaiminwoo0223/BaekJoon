# 베라의 패션
import sys

n = int(sys.stdin.readline())
numbers = list(range(n))
result = 0

for number in numbers:
    result += number

print(2 * result)
