# 크리스마스 선물
import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    presents = list(map(int, sys.stdin.readline().split()))
    if presents[0] != 0:
        for i in range(1, len(presents)):
            heapq.heappush(heap, -presents[i])
    else:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(-1)
