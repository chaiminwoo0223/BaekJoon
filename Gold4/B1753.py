# 최단경로
# 다익스트라 알고리즘
# Python의 heapq는 리스트나 튜플이 들어올 때, 첫 번째 요소를 기준으로 최소 힙을 구성합니다.
import heapq
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

# 우선순위 큐
queue = []
heapq.heappush(queue, [0, K])

# 거리 초기화
result = [float('inf')] * (V+1)
result[K] = 0

while queue:
    cost, node = heapq.heappop(queue)

    if cost > result[node]:
        continue

    for next_node, next_cost in graph[node]:
        new_cost = cost + next_cost

        if new_cost < result[next_node]:
            result[next_node] = new_cost
            heapq.heappush(queue, [new_cost, next_node])

for i in range(1, V+1):
    if result[i] != float('inf'):
        print(result[i])
    else:
        print("INF")
