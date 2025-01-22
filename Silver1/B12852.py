# 1로 만들기 2
# 다이나믹 프로그래밍
# 최솟값
from collections import deque
import sys

n = int(sys.stdin.readline())
visited = [0] * (n+1) # 핵심
q = deque()

def bfs():
    while q:
        x, numbers = q.popleft()
        numbers = numbers + [x] # 핵심
        visited[x] = 1

        if x == 1:
            print(len(numbers) - 1)
            print(*numbers)
            break
        if x % 3 == 0 and visited[x // 3] == 0:
            q.append([x // 3, numbers])
        if x % 2 == 0 and visited[x // 2] == 0:
            q.append([x // 2, numbers])
        if x - 1 > 0 and visited[x - 1] == 0:
            q.append([x - 1, numbers])

q.append([n, []])
bfs()
