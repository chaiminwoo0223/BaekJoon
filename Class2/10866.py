# 덱
from collections import deque
import sys
n = int(sys.stdin.readline())
deque = deque()

for i in range(n):
    command = sys.stdin.readline()
    if "push" in command:
        if "front" in command:
            deque.appendleft(int(command[11:]))
        else:
            deque.append(int(command[10:]))
    elif "pop" in command:
        if len(deque) == 0:
            print(-1)
        elif "front" in command:
            print(deque.popleft())
        else:
            print(deque.pop())
    elif "size" in command:
        print(len(deque))
    elif "empty" in command:
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif "front" in command:
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    elif "back" in command:
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])