# 최소 힙
import sys
import heapq # 핵심

n = int(sys.stdin.readline())
min_heap = []

for i in range(n):
    x = int(sys.stdin.readline())

    if x == 0:
        if len(min_heap) == 0:
            print(0)
        else:
            print(heapq.heappop(min_heap))
    else:
        heapq.heappush(min_heap, x)
    