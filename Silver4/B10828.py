# 스택
import sys # 핵심: input()과 비교했을 때, 속도가 더 빠르다!
n = int(sys.stdin.readline())
stack = []

for i in range(n):
    command = sys.stdin.readline()
    if "push" in command:
        stack.append(int(command[5:]))
    elif "pop" in command:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif "size" in command:
        print(len(stack))
    elif "empty" in command:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif "top" in command:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])