# 숨바꼭질 2
# 반례: 시작지와 목적지가 같은 경우 0이 되어야 한다.
from collections import deque

n, k = map(int, input().split())
visited = [-1] * 100001
q = deque([n])
visited[n] = 0
cnt = 0

def bfs():
    global cnt

    while q:
        x = q.popleft()

        if x == k:
            cnt += 1

        for next in (x-1, x+1, x*2):
            if 0 <= next < 100001 and (visited[next] == -1 or visited[next] == visited[x] + 1): # 핵심
                q.append(next)
                visited[next] = visited[x] + 1

bfs()

print(visited[k])
print(cnt)
