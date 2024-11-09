# 쇠막대기
import sys

s = sys.stdin.readline().rstrip()
stack = []
count = 0

for i in range(len(s)):
    if s[i] == "(":
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1] == "(":
            count += len(stack)
        else:
            count += 1
print(count)
