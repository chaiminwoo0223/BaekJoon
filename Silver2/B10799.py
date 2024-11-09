# 쇠막대기
import sys

s = list(map(str, sys.stdin.readline().split()))
stack = []
count = 0

for i in len(s):
    if s[i] == "(":
        stack.append(s[i])
    else:
        if s[i] == "(":
            stack.pop()
            count += len(stack)
        else:
            stack.pop()
            count += 1

print(count)
