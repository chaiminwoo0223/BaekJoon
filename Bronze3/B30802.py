# 웰컴 키트
import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
t, p = map(int, sys.stdin.readline().split())
count = 0

for i in range(6):
    if numbers[i] % t == 0:
        count += numbers[i] // t
    elif numbers[i] // t < 1:
        count += 1
    else:
        count += numbers[i] // t + 1

print(count)
print(n // p, n % p)
