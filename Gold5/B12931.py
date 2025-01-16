# 두 배 더하기
import sys

n = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
count = 0

while True:
    for i in range(n):
        if b[i] % 2 == 1:
            b[i] -= 1 # 핵심
            count += 1

    if sum(b) == 0:
        print(count)
        break
    else:
        for i in range(n):
            b[i] //= 2
        count += 1
