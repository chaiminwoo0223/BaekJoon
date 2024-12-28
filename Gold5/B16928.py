# 뱀과 사다리 게임
from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
board = [0] * 101
visited = [0] * 101
ladder = {} # 핵심
snake = {} # 핵심
q = deque()

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    ladder[x] = y

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    snake[u] = v     

def bfs():
    while q:
        start = q.popleft()
        for i in range(1, 7):
            next = start + i
            if 0 < next <= 100 and visited[next] == 0:
                if next in ladder:
                    next = ladder[next]
                if next in snake:
                    next = snake[next]
                if visited[next] == 0:
                    q.append(next)
                    visited[next] = 1
                    board[next] = board[start] + 1

q.append(1)
visited[1] = 1
bfs()

print(board[100])
