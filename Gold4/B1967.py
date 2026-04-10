# 트리의 지름
# DFS 2번
import sys

sys.setrecursionlimit(10**5)

# 가장 먼 지점 찾기
def dfs(start, distance):
    for x, y in tree[start]:
        if visited[x] == -1:
            visited[x] = y + distance
            dfs(x, visited[x])

input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

# 1) 가장 먼 지점을 먼저 찾기
visited = [-1] * (n+1)
visited[1] = 0
dfs(1, 0)

# 2) 가장 먼 지점을 다시 찾기
x = visited.index(max(visited))
visited = [-1] * (n+1)
visited[x] = 0
dfs(x, 0)

print(max(visited))
