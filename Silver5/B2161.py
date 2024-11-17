# 카드1
import sys

n = int(sys.stdin.readline())
numbers = list(range(1, n+1))
remain = []

while True:
    remain.append(numbers.pop(0))
    if len(numbers) > 1:
        numbers.append(numbers.pop(0))
    else:
        break

print(*remain, *numbers)
