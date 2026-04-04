# 파티
# 다익스트라 알고리즘 2번
# 함수 분리
import heapq
import sys

input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    start, end, time = map(int, input().split())
    graph[start].append([end, time])

def calculator(start):
    distance = [float('inf')] * (n+1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, [0, start])

    while queue:
        cost, node = heapq.heappop(queue)

        if distance[node] >= cost:

            for next_node, next_cost in graph[node]:
                new_cost = cost + next_cost

                if new_cost < distance[next_node]:
                    distance[next_node] = new_cost
                    heapq.heappush(queue, [new_cost, next_node])

    return distance

result = calculator(x) # 돌아가기
result[0] = 0

for i in range(1, n+1): # 참석하기
    if i != x:
        result[i] += calculator(i)[x]

print(max(result))
