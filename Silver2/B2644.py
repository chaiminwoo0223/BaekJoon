# 촌수계산 
from collections import deque
import sys

n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
family = [[0] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)
q = deque()

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    family[x][y] = 1
    family[y][x] = 1

def bfs():
    while q:
        x, count = q.popleft()
        visited[x] = 1
        
        if x == b:
            return count
        else:
            for next in range(1, n+1):
                if family[x][next] == 1 and visited[next] == 0:
                    q.append([next, count+1])

    return -1

q.append([a, 0])
print(bfs())
