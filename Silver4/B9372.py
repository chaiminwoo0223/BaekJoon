# 상근이의 여행
from collections import Counter
import sys

def dfs(v):
    global count

    visited[v] = 1
    count += 1
    
    for next in range(1, n+1):
        if visited[next] == 0 and graph[v][next] == 1:
            dfs(next)

for _ in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())
    graph = [[0] * (n+1) for _ in range(n+1)]
    visited = [0] * (n+1)
    counter = Counter()
    count = 0

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a][b] = 1
        graph[b][a] = 1
        counter[a] += 1
        counter[b] += 1

    dfs(counter.most_common()[-1][0])
    print(count - 1)
