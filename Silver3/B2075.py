# N번째 큰 수
# 최댓값, 최솟값 -> 최소힙
import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    numbers = list(map(int, sys.stdin.readline().split()))
    for number in numbers:
        if len(heap) != n:
            heapq.heappush(heap, number)
        else:
            heapq.heappushpop(heap, number)

print(heap[0])
