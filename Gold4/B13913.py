# 숨바꼭질 4
from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
visited = [0] * 100001
moved = [0] * 100001
q = deque()

def pathes(x):
    result = []
    temp = x

    for _ in range(visited[x]+1):
        result.append(temp)
        temp = moved[temp]
    print(*result[::-1])

def bfs():
    while q:
        x = q.popleft()

        if x == k:
            print(visited[x])
            pathes(x)
            return
        
        for next in (x-1, x+1, 2*x):
            if 0 <= next < 100001 and visited[next] == 0:
                q.append(next)
                visited[next] = visited[x] + 1
                moved[next] = x

q.append(n)
bfs()
