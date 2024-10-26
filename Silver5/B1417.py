# 국회의원 선거
import sys
import heapq

n = int(sys.stdin.readline())
dasom = int(sys.stdin.readline())
voters = []
count = 0

for _ in range(n-1):
    heapq.heappush(voters, -int(sys.stdin.readline())) # 최대힙

while voters and dasom <= -voters[0]:
    voter = -heapq.heappop(voters)
    voter -= 1
    dasom += 1
    count += 1
    heapq.heappush(voters, -voter)

print(count)
