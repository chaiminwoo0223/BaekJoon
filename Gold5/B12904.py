# A와 B
from sys import stdin

s = stdin.readline().rstrip()
t = stdin.readline().rstrip()

while len(s) < len(t):
    if t[-1] == "A":
        t = t[:-1]
    elif t[-1] == "B":
        t = t[:-1][::-1]

if s == t:
    print(1)
else:
    print(0)