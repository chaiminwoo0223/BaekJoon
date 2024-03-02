# 도키도키 간식드리미
from sys import stdin

n = int(stdin.readline())
standing = list(map(int, stdin.readline().split()))
stack = []
target = 1

while standing:
    if standing[0] == target:
        standing.pop(0)
        target += 1
    else:
        stack.append(standing.pop(0))
    while stack and stack[-1] == target:
        stack.pop()
        target += 1

print('Nice' if not stack else 'Sad')