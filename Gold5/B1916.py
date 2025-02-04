# 최소비용 구하기
# 다익스트라 알고리즘: 그래프에서 한 정점(시작점)으로부터 다른 모든 정점까지의 최단 경로
# 가중치가 있는 그래프
# 우선순위 큐(힙)
import sys
import heapq

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]

for _ in range(int(sys.stdin.readline())):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])

start, end = map(int, sys.stdin.readline().split())

# 최단 거리 초기화
distance = [float('inf')] * (n+1) # 무한대로 초기화
distance[start] = 0

# 힙
heap = []
heapq.heappush(heap, [start, 0])

while heap:
    node, cost = heapq.heappop(heap)

    # 이미 처리한 노드라면 무시
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
