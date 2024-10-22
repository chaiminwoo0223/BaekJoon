# 괄호의 값
import sys

s = sys.stdin.readline()
stack = []
result = 0
temp = 1

for i in range(len(s)):
    if s[i] == '(':
        temp *= 2
        stack.append(s[i])
    if s[i] == '[':
        temp *= 3
        stack.append(s[i])
    if s[i] == ')':
        if not stack or stack[-1] != '(':
            result = 0
            break
        if s[i-1] == '(':
            result += temp
        temp //= 2
        stack.pop()
    if s[i] == ']':
        if not stack or stack[-1] != '[':
            result = 0
            break
        if s[i-1] == '[':
            result += temp
        temp //= 3
        stack.pop()

if stack:
    print(0)
else:
    print(result)
