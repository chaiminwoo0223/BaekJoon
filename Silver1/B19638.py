# 센티와 마법의 뿅망치
import sys
import heapq

n, h, t = map(int, sys.stdin.readline().split())
giants = []
count = 0

for _ in range(n):
    heapq.heappush(giants, -int(sys.stdin.readline()))

for _ in range(t):
    giant = -heapq.heappop(giants)
    if giant != 1 and giant >= h:
        giant //= 2
        count += 1
        heapq.heappush(giants, -giant)
    else:
        heapq.heappush(giants, -giant)
        break

giant = -heapq.heappop(giants)
if giant < h:
    print("YES")
    print(count)
else:
    print("NO")
    print(giant)
