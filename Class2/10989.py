# 수 정렬하기
import sys
n = int(sys.stdin.readline()) # 핵심1
array = [0]*10001
for i in range(n):
    num = int(sys.stdin.readline())
    array[num] += 1 # 핵심2

for j in range(10001): # 핵심3
    if array[j] != 0:
        for k in range(array[j]):
            print(j)