# 문자열
import sys

x, y = sys.stdin.readline().rstrip().split()
result = []

for i in range(len(y)-len(x)+1):
    count = 0
    for j in range(len(x)):
        if x[j] != y[j+i]:
            count += 1
    result.append(count)

print(min(result))
