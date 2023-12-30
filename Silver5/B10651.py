# 좌표 정렬하기 2
import sys
n = int(sys.stdin.readline())
array = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    array.append([y, x])
array.sort()

for j in array:
    print(j[1], j[0])