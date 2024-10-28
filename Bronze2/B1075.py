# 나누기
import sys

n = sys.stdin.readline().rstrip()
f = int(sys.stdin.readline().rstrip())
n = n[:-2] + "00"

while int(n) % f != 0:
    n = str(int(n) + 1)
print(n[-2:])
