# DFS와 BFS
import sys

class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = [[0] * (n + 1) for _ in range(n + 1)]
        self.visited_dfs = [False] * (n + 1)
        self.visited_bfs = [False] * (n + 1)

    def add_edge(self, a, b):
        self.graph[a][b] = self.graph[b][a] = 1

    def dfs(self, v):
        self.visited_dfs[v] = True
        print(v, end=' ')
        for i in range(1, self.n + 1):
            if self.graph[v][i] == 1 and not self.visited_dfs[i]:
                self.dfs(i)

    def bfs(self, v):
        queue = [v]
        self.visited_bfs[v] = True
        while queue:
            v = queue.pop(0)
            print(v, end=' ')
            for i in range(1, self.n + 1):
                if not self.visited_bfs[i] and self.graph[v][i] == 1:
                    queue.append(i)
                    self.visited_bfs[i] = True

# 입력 처리
n, m, v = map(int, sys.stdin.readline().split())
graph = Graph(n)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph.add_edge(a, b)

# DFS와 BFS 실행
graph.dfs(v)
print()
graph.bfs(v)