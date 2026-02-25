# 최소비용 구하기
# 다익스트라 알고리즘: 그래프에서 한 정점(시작점)으로부터 다른 모든 정점까지의 최단 경로
# 우선순위 큐(힙)
import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
heap = []

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost]) # 핵심

start, end = map(int, input().split())

# 최단 거리 최소화
distance = [int(1e9)] * (n + 1)
distance[start] = 0

# 힙
heapq.heappush(heap, [start, 0])

while heap:
    node, cost = heapq.heappop(heap)

    # 이미 처리한 노드라면 무
    if cost > distance[node]:
        continue

    # 인접 노드 탐색
    for next_node, next_cost in graph[node]:
        new_cost = cost + next_cost

        # 업데이트
        if new_cost < distance[next_node]:
            distance[next_node] = new_cost
            heapq.heappush(heap, [next_node, new_cost])

print(distance[end])
