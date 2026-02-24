# A → B
import sys

input = sys.stdin.readline

a, b = map(int, input().split())
cnt = 0

while a < b:
    if b % 2 == 0:
        b //= 2
    elif ((b // 10) * 10 + 1) == b:
        b //= 10
    else:
        break

    cnt += 1

if a != b:
    print(-1)
else:
    print(cnt + 1)
