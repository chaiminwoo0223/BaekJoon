# 상근이의 여행
import sys

def dfs(v):
    global count
    visited[v] = 1
    count += 1
    for next in range(1, n+1):
        if visited[next] == 0 and graph[v][next] == 1:
            dfs(next)

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    graph = [[0] * (n+1) for _ in range(n+1)]
    visited = [0] * (n+1)
    number = set()
    count = 0

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a][b] = 1
        graph[b][a] = 1
        number.add(a)
        number.add(b)

    dfs(min(number))
    print(count - 1)
