# 숨바꼭질 2
from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
visited = [-1] * 100001
q = deque([(n)])
visited[n] = 0
count = 0

def bfs():
    global count

    while q:
        x = q.popleft()

        if x == k:
            count += 1
            
        for next in (x-1, x+1, 2*x):
            if 0 <= next < 100001:
                if visited[next] == -1 or visited[next] == visited[x] + 1: # 핵심
                    q.append(next)
                    visited[next] = visited[x] + 1

bfs()

print(visited[k])
print(count)
