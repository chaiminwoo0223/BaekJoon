# DSLR
# PyPy3
from collections import deque
import sys

t = int(sys.stdin.readline())

def bfs():
    while q:
        number, command = q.popleft()

        if number == b:
            print(command)
            break
        
        # D
        d = (number * 2) % 10000
        if visited[d] == 0:
            visited[d] = 1
            q.append([d, command + "D"])
        
        # S
        s = (number - 1) % 10000
        if visited[s] == 0:
            visited[s] = 1
            q.append([s, command + "S"])

        # L
        l = (number % 1000) * 10 + (number // 1000) # 핵심
        if visited[l] == 0:
            visited[l] = 1
            q.append([l, command + "L"])

        # R
        r = (number % 10) * 1000 + (number // 10) # 핵심
        if visited[r] == 0:
            visited[r] = 1
            q.append([r, command + "R"])

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    q = deque()
    q.append([a, ""]) # 핵심
    visited = [0] * 10001
    visited[a] = 1
    bfs()
