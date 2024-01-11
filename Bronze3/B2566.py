# 최댓값
import sys

maximum = -1
max_row = 0
max_col = 0

for i in range(9):
    row = list(map(int, sys.stdin.readline().split()))
    for j in range(9):
        if row[j] > maximum:
            maximum = row[j]
            max_row = i + 1
            max_col = j + 1

print(maximum)
print(max_row, max_col)