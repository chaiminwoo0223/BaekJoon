# 트리의 부모 찾기
from collections import deque
import sys

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)] # 핵심
parent = [0] * (n+1) # 핵심2

for _ in range(n-1):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs():
    q = deque([1])
    while q:
        current = q.popleft()
        for next in graph[current]: # 핵심3
            if parent[next] == 0:
                parent[next] = current
                q.append(next)

bfs()

for i in range(2, n+1):
    print(parent[i])
