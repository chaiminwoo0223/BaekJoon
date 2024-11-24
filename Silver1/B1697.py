# 숨바꼭질
from collections import deque
import sys

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            return visited[x]

        for i in (x-1, x+1, x*2):
            if 0 <= i < 100001 and not visited[i]:
                visited[i] = visited[x] + 1
                q.append(i)

n, k = map(int, sys.stdin.readline().split())
visited = [0] * 100001

print(bfs())
