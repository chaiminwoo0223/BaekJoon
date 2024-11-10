# 미로 탐색
# BFS
# 방향
from collections import deque
import sys

def bfs(l, r):
    q.append((l, r))
    while q:
        l, r = q.popleft()
        for i in range(4):
            nl = l + dl[i]
            nr = r + dr[i]
            if 0 <= nl < n and 0 <= nr < m and miro[nl][nr] == 1:
                q.append((nl, nr))
                miro[nl][nr] = miro[l][r] + 1
    return miro[n-1][m-1]

n, m = map(int, sys.stdin.readline().split())
miro = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
dl = [0, 1, 0, -1]
dr = [1, 0, -1, 0]
q = deque()

print(bfs(0, 0))
