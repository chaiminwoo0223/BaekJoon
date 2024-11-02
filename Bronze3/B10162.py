# 전자레인지
import sys

t = int(sys.stdin.readline())
a = 300
b = 60
c = 10
button = ["", "", ""]

if t % c != 0:
    print(-1)
else:
    button[0] = str(t // a)
    t %= a
    button[1] = str(t // b)
    t %= b
    button[2] = str(t // c)
    print(" ".join(button))
