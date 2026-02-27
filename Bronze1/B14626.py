# ISBN
import sys

input = sys.stdin.readline

numbers = input().rstrip()
c = 0
t = 0

for i, number in enumerate(numbers):
    if number.isdigit():
        if i % 2 == 0:
            t += int(number)
        else:
            t += (int(number) * 3)
    else:
        if i % 2 == 1:
            c = 3
        else:
            c = 1

for j in range(11):
    if (t + j * c) % 10 == 0:
        print(j)
        break
