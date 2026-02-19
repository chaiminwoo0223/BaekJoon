# 1로 만들기 2
from collections import deque

n = int(input())
q = deque([n])
visited = [-1] * 1000001
moved = [0] * 1000001

visited[n] = 0
result = [1]
t = 1

while q:
    x = q.popleft()

    if x == 1:
        print(visited[x])
        break

    for i in (3, 2):
        if x % i == 0 and visited[x // i] == -1:
            q.append(x // i)
            visited[x // i] = visited[x] + 1
            moved[x // i] = x

    if visited[x - 1] == -1:
        q.append(x - 1)
        visited[x - 1] = visited[x] + 1
        moved[x - 1] = x

for _ in range(visited[1]):
    t = moved[t]
    result.append(t)

print(*result[::-1])
