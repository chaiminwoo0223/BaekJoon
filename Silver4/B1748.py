# 수 이어 쓰기 1
import sys

n = sys.stdin.readline().rstrip()
result = 0

for i in range(1, len(n)):
    result += int('9' + (i-1) * '0') * i
result += (int(n) - 10**(len(n)-1) + 1) * len(n)

print(result)
