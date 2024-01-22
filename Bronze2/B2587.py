# 대표값2
from statistics import mean
import sys

numbers = []

for _ in range(5):
    numbers.append(int(sys.stdin.readline()))

print(mean(numbers))
print(sorted(numbers)[2])