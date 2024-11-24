# 방 번호
import sys

n = sys.stdin.readline().rstrip()
numbers = [0] * 10 # 핵심

for i in n:
    number = int(i)
    if number in (6, 9):
        if numbers[6] == numbers[9]:
            numbers[6] += 1
        else:
            numbers[9] += 1
    else:
        numbers[number] += 1

print(max(numbers))
