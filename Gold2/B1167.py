# 트리의 지름
# 숨겨진 조건: 루트 노드는 항상 1이다.
import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

V = int(input())
tree = [[] for _ in range(V+1)]

for _ in range(V):
    X = list(map(int, input().split()))

    for i in range(1, len(X), 2):
        if X[i] == -1:
            break

        tree[X[0]].append((X[i], X[i+1]))

def dfs(n, distance):
    visited[n] = distance

    for next_node, next_distance in tree[n]:
        if visited[next_node] == -1:
            dfs(next_node, distance + next_distance)

# 1) 가장 먼 지점을 먼저 찾기
visited = [-1] * (V+1)
visited[1] = 0
dfs(1, 0)

# 2) 가장 먼 지점을 다시 찾기
x = visited.index(max(visited))
visited = [-1] * (V+1)
visited[x] = 0
dfs(x, 0)

print(max(visited))
