# 큐
from collections import deque
import sys
n = int(sys.stdin.readline())
queue = deque()

for i in range(n):
    command = sys.stdin.readline()
    if "push" in command:
        queue.append(int(command[5:]))
    elif "pop" in command: # 앞 = 왼쪽
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif "size" in command:
        print(len(queue))
    elif "empty" in command:
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif "front" in command: # 앞 = 왼쪽
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif "back" in command: # 뒤 = 오른쪽
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])