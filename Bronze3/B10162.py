# 전자레인지
import sys

t = int(sys.stdin.readline())
button = [0, 0, 0]

while t > 0:
    if t - 300 >= 0:
        t -= 300
        button[0] += 1
    elif t - 60 >= 0:
        t -= 60
        button[1] += 1
    else:
        t -= 10
        button[2] += 1

if t >= 0:
    print(*button)
else:
    print(-1)
