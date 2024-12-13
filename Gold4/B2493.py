# 탑
import sys
n = int(sys.stdin.readline())
buliding = list(map(int, sys.stdin.readline().split()))
stack = []
result = [0] * n

for i in range(n):
    while stack and buliding[stack[-1]] <= buliding[i]: # 핵심
        stack.pop()
    if stack:
        result[i] = stack[-1] + 1
    stack.append(i)

print(*result)
