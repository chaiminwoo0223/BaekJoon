# 시각
import sys

def time(t):
    if len(str(t)) == 1:
        return "0" + str(t)
    else:
        return str(t)

n, k = map(int, sys.stdin.readline().split())
result = 0

for h in range(n+1):
    hour = time(h)
    for m in range(60):
        minute = time(m)
        for s in range(60):
            second = time(s)
            if str(k) in hour or str(k) in minute or str(k) in second:
                result += 1
print(result)
