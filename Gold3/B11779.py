# 최소비용 구하기 2
# 다익스트라 알고리즘
# Python의 heapq는 리스트나 튜플이 들어올 때, 첫 번째 요소를 기준으로 최소 힙을 구성합니다.
import heapq
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

start, end = map(int, input().split())

queue = []
heapq.heappush(queue, [0, start, [start]]) # cost, node, path
result = [int(1e9)] * (n+1)
result[start] = 0
final_result = [int(1e9), 0, []]

while queue:
    cost, node, path = heapq.heappop(queue)

    if node == end and cost < final_result[0]:
        final_result = [cost, len(path), path]

    if cost > result[node]:
        continue

    for next_node, next_cost in graph[node]:
        new_cost = cost + next_cost
        new_path = path + [next_node]

        if new_cost < result[next_node]:
            result[next_node] = new_cost
            heapq.heappush(queue, [new_cost, next_node, new_path])

print(final_result[0])
print(final_result[1])
print(*final_result[2])
