# 최대 힙
import sys
import heapq # 핵심

n = int(sys.stdin.readline())
max_heap = []

for i in range(n):
    x = int(sys.stdin.readline())

    if x == 0:
        if len(max_heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(max_heap))
    else:
        heapq.heappush(max_heap, -x)
    