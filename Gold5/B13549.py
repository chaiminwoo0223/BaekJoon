# 숨바꼭질 3
# count X -> visited O
from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
q = deque([(n)])
visited = [0] * 100001

def calculator(next):
    if 0 <= next < 100001 and visited[next] == 0:
        q.append(next)

def bfs():
    while q:
        x = q.popleft()
        xx = 2 * x

        if x == k or 2 * x == k:
            return visited[x]
        
        if 0 <= xx < 100001 and visited[xx] == 0:
            visited[xx] = visited[x]
            q.append(xx)
        
        for next in (x-1, x+1):
            if 0 <= next < 100001 and visited[next] == 0:
                visited[next] = visited[x] + 1
                q.append(next)
        
print(bfs())
