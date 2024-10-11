# ATM
import sys

n = int(sys.stdin.readline())
p = sorted(map(int, sys.stdin.readline().split()))
stack = [0]
total = []

for t in p:
    stack.append(t)
    total.append(sum(stack))

print(sum(total))
