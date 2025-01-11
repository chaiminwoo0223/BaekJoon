# 트리의 부모 찾기
# 트리의 루트 = 1
from collections import deque
import sys

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)] # 핵심
visited = [0] * (n+1)
q = deque()

for _ in range(n-1):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

def tree():
    while q:
        root = q.popleft()

        for next in graph[root]:
            if visited[next] == 0:
                q.append(next)
                visited[next] = root

q.append(1)
tree()
       
for i in range(2, n+1):
    print(visited[i])
