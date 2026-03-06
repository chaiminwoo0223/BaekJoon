# 쇠막대기
import sys

input = sys.stdin.readline()

x = input.rstrip()
stack = []
cnt = 0

for i in range(len(x)):
    if x[i] == '(':
        stack.append(x[i])
    else:
        stack.pop()

        if x[i-1] == '(':
            cnt += len(stack)
        else:
            cnt += 1

print(cnt)
