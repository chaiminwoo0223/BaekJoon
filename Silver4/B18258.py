# 큐 2
from collections import deque
import sys

n = int(input())
Deque = deque()

for i in range(n):
  cmd = sys.stdin.readline().split()
  if cmd[0] == "push":
    Deque.append(cmd[1])
  elif cmd[0] == "pop":
    if len(Deque) == 0:
      print(-1)
    else:
      print(Deque.popleft())
  elif cmd[0] == "size":
    print(len(Deque))
  elif cmd[0] == "empty":
    if len(Deque) == 0:
      print(-1)
    else:
      print(0)
  elif cmd[0] == "front":
    if len(Deque) == 0:
      print(-1)
    else:
      print(Deque[0])
  elif cmd[0] == "back":
    if len(Deque) == 0:
      print(-1)
    else:
      print(Deque[-1])
