# AC
from collections import deque
import sys

t = int(sys.stdin.readline())
result = []

for _ in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    x = sys.stdin.readline().rstrip()[1:-1].split(",")
    reverse = False
    error = False
    
    if n != 0:
        x = deque(x)
    else:
        x = deque()

    for i in range(len(p)):
        if p[i] == "R":
            reverse = not reverse
        else:
            if len(x) < 1:
                result.append("error")
                error = True
                break
            else:
                if reverse:
                    x.pop()
                else:
                    x.popleft()
    
    if not error:
        if reverse:
            x.reverse()
        result.append("[" + ",".join(x) + "]")

for r in result:
    print(r)
