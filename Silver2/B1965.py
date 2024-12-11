# 상자넣기
import sys

n = int(sys.stdin.readline())
box = list(map(int, sys.stdin.readline().split()))
numbers = [1] * n

for i in range(1, n):
    for j in range(i):
        if box[i] > box[j]:
            numbers[i] = max(numbers[i], numbers[j]+1)

print(max(numbers))
