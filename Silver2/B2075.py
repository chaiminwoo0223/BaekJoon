# N번째 큰 수
import sys
import heapq

n = int(sys.stdin.readline())
heap = []

numbers = list(map(int, sys.stdin.readline().split()))
for number in numbers:
    heapq.heappush(heap, number)

for _ in range(n-1):
    numbers = list(map(int, sys.stdin.readline().split()))
    for number in numbers:
        if heap[0] < number:
            heapq.heappushpop(heap, number)

print(heap[0])
