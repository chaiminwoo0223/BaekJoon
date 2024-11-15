# 파도반 수열
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    numbers = [1, 1, 1, 2, 2] + [0] * 96

    if n < 4:
        print(numbers[n-1])
    else:
        for i in range(5, n+1):
            numbers[i] = numbers[i-1] + numbers[i-5]
        print(numbers[n-1])
