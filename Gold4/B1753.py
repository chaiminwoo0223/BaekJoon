# 최단경로
# 다익스트라 알고리즘: 그래프에서 한 정점(시작점)으로부터 다른 모든 정점까지의 최단 경로
# heapq는 첫 번째 원소를 기준으로 정렬
import sys
import heapq

v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
graph = [[] for _ in range(v+1)]

for _ in range(e):
    u, c, w = map(int, sys.stdin.readline().split())
    graph[u].append([c, w])

# 최단 거리 초기화
distance = [float('INF')] * (v+1)
distance[k] = 0

# 힙 초기화
heap = []
heapq.heappush(heap, [0, k]) # 핵심: 거리를 기준으로 정렬

while heap:
    cost, node = heapq.heappop(heap)

    # 이미 처리한 노드라면 무시
    if cost > distance[node]:
        continue
    
    # 인접 노드 탐색
    for next_node, next_cost in graph[node]:
        new_cost = cost + next_cost

        # 업데이트
        if new_cost < distance[next_node]:
            distance[next_node] = new_cost
            heapq.heappush(heap, [new_cost, next_node])

for i in range(1, v+1):
    if str(distance[i]) == 'inf':
        print('INF')
    else:
        print(distance[i])
