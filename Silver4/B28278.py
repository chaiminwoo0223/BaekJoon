# 스택 2
import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    cmd = sys.stdin.readline().rstrip()
    if cmd.startswith("1"):
        stack.append(int(cmd[2:]))
    elif cmd.startswith("2"):
        print(stack.pop() if stack else -1)
    elif cmd.startswith("3"):
        print(len(stack))
    elif cmd.startswith("4"):
        print(1 if not stack else 0)
    elif cmd.startswith("5"):
        print(stack[-1] if stack else -1)
    else:
        pass