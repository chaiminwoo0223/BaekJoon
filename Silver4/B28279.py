# 덱 2
from collections import deque
import sys

n = int(sys.stdin.readline())
deq = deque()

for _ in range(n):
    cmd = sys.stdin.readline().rstrip()
    if cmd.startswith("1"):
        deq.appendleft(int(cmd[2:]))
    elif cmd.startswith("2"):
        deq.append(int(cmd[2:]))
    elif cmd.startswith("3"):
        print(deq.popleft() if deq else -1)
    elif cmd.startswith("4"):
        print(deq.pop() if deq else -1)
    elif cmd.startswith("5"):
        print(len(deq))
    elif cmd.startswith("6"):
        print(1 if not deq else 0)
    elif cmd.startswith("7"):
        print(deq[0] if deq else -1)
    elif cmd.startswith("8"):
        print(deq[-1] if deq else -1)
    else:
        pass