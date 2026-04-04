# 플로이드 2
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
pathes = []

for i in range(1, n+1):
    # 거리 초기화
    distance = [float('inf')] * (n+1)
    distance[i] = 0

    path = [[] for _ in range(n + 1)]
    path[i] = [i]

    heapq.heappush(queue, (0, i))

    while queue:
        cost, node = heapq.heappop(queue)

        if cost > distance[node]:
            continue

        for next_node, next_cost in graph[node]:
            new_cost = cost + next_cost

            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(queue, (new_cost, next_node))
                path[next_node] = path[node] + [next_node]

    print(*[r if r != float('inf') else 0 for r in distance[1:]])
    pathes.append(path)

for path in pathes:
    for p in path[1:]:
        if len(p) in (0, 1):
            print(0)
        else:
            print(len(p), *p)
