# 알고리즘 수업 - 깊이 우선 탐색 1
import sys
sys.setrecursionlimit(200000)

n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
count = 1

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(x):
    global count

    for next in sorted(graph[x]):
        if visited[next] == 0:
            count += 1
            visited[next] = count
            dfs(next)

visited[r] = 1
dfs(r)

for i in range(1, n+1):
    print(visited[i])
