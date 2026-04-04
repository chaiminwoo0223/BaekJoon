# 플로이드
# Python의 heapq는 리스트나 튜플이 들어올 때, 첫 번째 요소를 기준으로 최소 힙을 구성합니다.
import heapq
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())

    finished = 0

    if graph[a]:
        for i, x in enumerate(graph[a]): # 최솟값
            if x[0] == b:
                graph[a][i] = (b, min(c, x[1]))
                finished = 1
                break

    if finished:
        continue
    else:
        graph[a].append((b, c))

queue = [] # 우선순위 큐

for i in range(1, n+1):
    result = [float('inf')] * (n+1) # 거리 초기화
    result[i] = 0

    heapq.heappush(queue, (0, i))

    while queue:
        cost, node = heapq.heappop(queue)

        if cost > result[node]:
            continue

        for next_node, next_cost in graph[node]:
            new_cost = cost + next_cost

            if new_cost < result[next_node]:
                result[next_node] = new_cost
                heapq.heappush(queue, (new_cost, next_node))

    print(*[r if r != float('inf') else 0 for r in result[1:]])
