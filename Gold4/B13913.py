# 숨바꼭질 4
from collections import deque

n, k = map(int, input().split())
visited = [0] * 100001
moved = [0] * 100001
q = deque([n])

def bfs():
    while q:
        x = q.popleft()

        if x == k:
            print(visited[x])
            path(x)
            break

        for next in (x-1, x+1, x*2):
            if 0 <= next < 100001 and not visited[next]:
                q.append(next)
                visited[next] = visited[x] + 1
                moved[next] = x

def path(x):
    result = []
    t = x

    for _ in range(visited[x]+1):
        result.append(t)
        t = moved[t]

    print(*result[::-1])

bfs()
