# 연결 요소의 개수
import sys

sys.setrecursionlimit(1000**2) # 런타임 에러(RecursionError)를 방지하기 위해 재귀 한도를 설정

def dfs(v):
    visited[v] = True
    for g in graph[v]:
        if not visited[g]:
            visited[g] = True
            dfs(g)

n, m = map(int, sys.stdin.readline().split())
graph = list([] for _ in range(n+1))
visited = [False] * (n+1)
count = 0

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):
    if not visited[i]:
        count += 1
        dfs(i)

print(count)
