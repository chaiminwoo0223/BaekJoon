# 두 배 더하기
import sys

n = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
count = 0

while True:
    # 짝수 만들기
    for i in range(n):
        if b[i] % 2 == 1:
            b[i] -= 1
            count += 1

    if max(b) == 0:
        print(count)
        break
    else:
        for i in range(n):
            b[i] //= 2
        count += 1
