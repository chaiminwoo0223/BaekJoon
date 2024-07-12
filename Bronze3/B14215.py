# 세 막대
import sys

def check_triangle(sides):
    max_length = max(sides)
    other_lengths = sum(sides) - max_length
    return max_length < other_lengths

a, b, c = map(int, sys.stdin.readline().strip().split())
max_side = 0

for i in range(a, 0, -1):
    for j in range(b, 0, -1):
        for k in range(c, 0, -1):
            sides = [i, k, j]
            if check_triangle(sides) == True:
                if max_side < sum(sides):
                    max_side = sum(sides)
            else:
                continue

print(max_side)
