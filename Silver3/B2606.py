# 바이러스
# BFS
from collections import deque
import sys

def bfs():
    global count # 전역변수 수정 가능

    while q:
        current = q.popleft()
        for next in range(1, n+1):
            if not visited[next] and graph[current][next]:
                visited[next] = True
                q.append(next)
                count += 1
    return count

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[False] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)
q = deque()
count = 0

# 그래프 초기화
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = True
    graph[b][a] = True

q.append(1)
visited[1] = True
print(bfs())
