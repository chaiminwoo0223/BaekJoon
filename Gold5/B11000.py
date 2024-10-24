# 강의실 배정
import sys
import heapq # 핵심

n = int(sys.stdin.readline())
classrooms = []
heap = []

for _ in range(n):
    classrooms.append(list(map(int, sys.stdin.readline().rstrip().split())))
classrooms = sorted(classrooms)

heapq.heappush(heap, classrooms[0][1]) # 첫번째 강의가 끝나는 시간
for i in range(1, n):
    if heap[0] > classrooms[i][0]:
        heapq.heappush(heap, classrooms[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, classrooms[i][1])

print(len(heap))
