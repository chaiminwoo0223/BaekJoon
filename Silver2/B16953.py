# A → B
import sys

a, b = map(int, sys.stdin.readline().split())
count = 0

while a < b:
    if b % 2 == 0:
        b //= 2
    elif b % 2 == 1:
        if str(b)[-1] == '1':
            b = int(str(b)[:-1])
        else:
            break

    count += 1

if a == b:
    print(count+1)
else:
    print(-1)
