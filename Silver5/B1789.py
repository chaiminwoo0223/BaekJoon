# 수들의 합
# 최대한 작은 수를 더해서 S를 만들어야지만 N(count)가 최대가 될 수 있다.
# S = 200, N = 19, numbers = [2, 3, 4, 5, ..., 19, 21] or [1, 3, 4, 5, ..., 19, 22] or [1, 2, 4, 5, ..., 19, 23]
import sys

s = int(sys.stdin.readline())
result = 0
count = 0

for i in range(1, s+1):
    if result + i > s:
        break
    else:
        result += i
        count += 1
print(count)
