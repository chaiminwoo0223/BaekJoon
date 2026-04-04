# 최소비용 구하기
# 다익스트라 알고리즘
# Python의 heapq는 리스트나 튜플이 들어올 때, 첫 번째 요소를 기준으로 최소 힙을 구성합니다.
import heapq
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

start, end = map(int, input().split())

# 우선순위 큐
queue = []
heapq.heappush(queue, [0, start])

# 거리 초기화
result = [float('inf')] * (n + 1)
result[start] = 0

while queue:
    cost, node = heapq.heappop(queue)

    # 비용이 작지 않으면 무시
    if cost > result[node]:
        continue

    # 인접 노드 탐색
    for next_node, next_cost in graph[node]:
        new_cost = cost + next_cost

        # 우선순위 큐 대입
        if new_cost < result[next_node]:
            result[next_node] = new_cost
            heapq.heappush(queue, [new_cost, next_node])

print(result[end])
