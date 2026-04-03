# 최소비용 구하기
# 다익스트라 알고리즘
import heapq
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
queue = []

for _ in range(m):
    x, y, cost = map(int, input().split())
    graph[x].append([y, cost]) # 핵심

start, end = map(int, input().split())

heapq.heappush(queue, [start, 0]) # 우선순위 큐

# 거리 초기화
result = [float('inf')] * (n+1)
result[start] = 0

while queue:
    node, cost = heapq.heappop(queue)

    # 이미 처리한 노드라면 무시
    if cost > result[node]:
        continue

    # 인접 노드 탐색
    for next_node, next_cost in graph[node]:
        new_cost = cost + next_cost

        # 우선순위 큐 대입
        if new_cost < result[next_node]:
            result[next_node] = new_cost
            heapq.heappush(queue, [next_node, new_cost])

print(result[end])
