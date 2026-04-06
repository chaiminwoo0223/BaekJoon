# 서강그라운드
# 서강그라운드에서 1등을 하면 보상으로 치킨을 주는데, 예은이는 단 한번도 치킨을 먹을 수가 없었다.
from collections import deque
import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
T = [0] + list(map(int, input().split())) # 각 구역에 있는 아이템의 수 t
graph = [[] for _ in range(n+1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append([b, l])
    graph[b].append([a, l])

# 큐
queue = deque()

def bfs(x):
    queue.append([0, x, T[x]])
    items = [0] * (n + 1)

    while queue:
        distance, node, item = queue.popleft()

        items[node] = item

        for next_node, next_distance in graph[node]:
            new_distance = distance + next_distance

            if new_distance <= m:
                queue.append([new_distance, next_node, T[next_node]])

    return sum(items)

print(max([bfs(i) for i in range(1, n+1)]))
