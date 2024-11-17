# 촌수계산
from collections import deque
import sys

def bfs(a, b):
    q = deque([a])
    while q:
        person = q.popleft()
        if person == b:
            return visited[b]
        for g in graph[person]:
            if visited[g] == 0:
                q.append(g)
                visited[g] = visited[person] + 1
    return -1

n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
relations = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)] # 핵심

for relation in relations: # 양방향 연결
    x, y = relation
    graph[x].append(y)
    graph[y].append(x)

print(bfs(a, b))
