# 센티와 마법의 뿅망치
# 힙
import sys
import heapq

n, h, t = map(int, sys.stdin.readline().split())
giants = []
count = 0

for _ in range(n):
    heapq.heappush(giants, -int(sys.stdin.readline())) # 핵심

for _ in range(t):
    giant = -heapq.heappop(giants)
    if giant >= h and giant != 1:
        heapq.heappush(giants, -(giant // 2))
        count += 1 # 핵심
    else:
        heapq.heappush(giants, -giant)
        break

giant = -heapq.heappop(giants)
if giant >= h:
    print("NO")
    print(giant)
else:
    print("YES")
    print(count)
