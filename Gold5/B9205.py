# 맥주 마시면서 걸어가기
# 경유
from collections import deque
import sys

def bfs():
    q = deque()
    q.append(home)

    while q:
        x1, y1 = q.popleft()
        if abs(x1 - festival[0]) + abs(y1 - festival[1]) <= 1000: # 핵심
            print("happy")
            return
        for i in range(n):
            if visited[i] == 0:
                x2, y2 = store[i]
                if abs(x1 - x2) + abs(y1 - y2) <= 1000:
                    q.append([x2, y2])
                    visited[i] = 1

    print("sad")
    return

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline()) # 맥주를 파는 편의점 개수
    home = list(map(int, sys.stdin.readline().split()))
    store = sorted(list(map(int, sys.stdin.readline().split())) for _ in range(n))
    festival = list(map(int, sys.stdin.readline().split()))
    visited = [0] * n
    bfs()
