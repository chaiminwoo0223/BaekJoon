# 숨바꼭질 3
from collections import deque

n, k = map(int, input().split())
visited = [0] * 100001
q = deque([n])

def bfs():
    while q:
        x = q.popleft()
        xx = 2 * x

        if x == k or xx == k:
            return visited[x]

        if 0 <= xx < 100001 and not visited[xx]:
            q.append(xx)
            visited[xx] = visited[x]

        for next in (x - 1, x + 1):
            if 0 <= next < 100001 and not visited[next]:
                q.append(next)
                visited[next] = visited[x] + 1

print(bfs())
