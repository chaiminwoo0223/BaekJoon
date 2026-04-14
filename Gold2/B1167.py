# 트리의 지름
import sys

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

result = []

for i in range(1, V+1):
    visited = [-1] * (V+1)
    dfs(i, 0)

    result.append(max(visited))

print(max(result))
