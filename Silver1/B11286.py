# 절댓값 힙
import sys
import heapq

n = int(sys.stdin.readline())
heap_q = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(heap_q, (abs(x), x)) # 핵심
    else:
        if len(heap_q) != 0:
            print(heapq.heappop(heap_q)[1])
        else:
            print(0)
