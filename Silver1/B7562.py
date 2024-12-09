# 나이트의 이동
# 누적합
from collections import deque
import sys

def bfs(e, f, g, h, i):
    chess = [[0] * i for _ in range(i)]
    q = deque()
    q.append([e, f])
    chess[e][f] = 1 # 핵심: 방문 표시

    while q:
        x, y = q.popleft()
        if x == g and y == h:
            return chess[x][y] - 1 # 핵심2: 시작 지점 제외
        
        for j in range(8):
            tx = x + dx[j]
            ty = y + dy[j]
            if 0 <= tx < i and 0 <= ty < i and chess[tx][ty] == 0:
                chess[tx][ty] = chess[x][y] + 1 # 핵심3: 이동 횟수 갱신
                q.append([tx, ty])
    return -1

t = int(sys.stdin.readline())
dx = [-2, -2, -1, 1, 2, 2, 1, -1]
dy = [-1, 1, 2, 2, 1, -1, -2, -2]

for _ in range(t):
    i = int(sys.stdin.readline())
    a, b = map(int, sys.stdin.readline().split())
    c, d = map(int, sys.stdin.readline().split())
    print(bfs(a, b, c, d, i))
