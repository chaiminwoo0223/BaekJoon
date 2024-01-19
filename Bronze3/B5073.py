# 삼각형과 세 변
import sys

def check_triangle(sides):
    max_length = max(sides)
    other_lengths = sum(sides) - max(sides)

    if max_length < other_lengths:
        return True
    else:
        return False

while True:
    sides = list(map(int, sys.stdin.readline().split()))

    if len(set(sides)) == 1 and sides[0] == 0:
        break
    elif check_triangle(sides) == False:
        print("Invalid")
    elif len(set(sides)) == 1:
        print("Equilateral")
    elif len(set(sides)) == 2:
        print("Isosceles")
    else:
        print("Scalene")