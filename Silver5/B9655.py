# 돌 게임
import sys

n = int(sys.stdin.readline())
count = 0

while n != 0:
    if n >= 3:
        n -= 3
    else:
        n -= 1
    count += 1

if count % 2 == 1:
    print("SK")
else:
    print("CY")
