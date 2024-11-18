# 거스름돈
# 작은 것부터
import sys

n = int(sys.stdin.readline())
result = 0

while n > 0:
    if n % 5 == 0:
        result += n // 5
        break
    else:
        n -= 2
        result += 1

if n < 0:
    print(-1)
else:
    print(result)
