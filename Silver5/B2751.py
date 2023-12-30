# 수 정렬하기 2
import sys
n = int(sys.stdin.readline())
array = []

for i in range(n):
    num = int(sys.stdin.readline())
    array.append(num)    
result = sorted(set(array))
for j in result:
    print(j)