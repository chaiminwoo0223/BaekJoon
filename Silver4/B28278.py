# 스택 2
import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    cmd = sys.stdin.readline().rstrip()
    if "1" in cmd:
        stack.append(int(cmd[2:]))
    elif "2" in cmd:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif "3" in cmd:
        print(len(stack))
    elif "4" in cmd:
        if not stack:
            print(1)
        else:
            print(0)
    elif "5" in cmd:
        if stack:
            print(stack[-1])
        else:
            print(-1)
    else:
        pass