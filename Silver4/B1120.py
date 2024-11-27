# 문자열
# a가 b 속에서 얼마나 많은 부분이 같은가?
import sys

a, b = map(str, sys.stdin.readline().split())
result = []

for i in range(len(b)-len(a)+1):
    count = 0
    for j in range(len(a)):
        if a[j] != b[i+j]:
            count += 1
        result.append(count)

print(min(result))
