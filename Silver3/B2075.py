# N번째 큰 수
# 최소힙
# 메모리초과 해결 -> 입력 데이터를 저장하지 말고 처리해야 함
import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for i in range(n):
    numbers = list(map(int, sys.stdin.readline().split()))
    for number in numbers:
        if len(heap) == n:
            heapq.heappushpop(heap, number)
        else:
            heapq.heappush(heap, number)
    
print(heapq.heappop(heap))
