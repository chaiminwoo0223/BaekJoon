# 아이들과 선물 상자
import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
presents = []
for present in list(map(int, sys.stdin.readline().split())):
    heapq.heappush(presents, -present)
hopes = list(map(int, sys.stdin.readline().split()))

for _ in range(m):
    present = -heapq.heappop(presents)
    hope = hopes.pop(0)
    remain = present - hope
    if present >= hope:
        heapq.heappush(presents, -remain)
    else:
        hopes.append(hope)
        break

if hopes:
    print(0)
else:
    print(1)
