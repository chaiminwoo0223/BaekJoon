# 1로 만들기 2
from collections import deque
import sys

n = int(sys.stdin.readline())

def bfs(x):
    visited = [0] * (n+1) # n + 1 크기의 방문 체크 배열 생성
    q = deque([[x, []]]) # 핵심: 큐에 초깃값과 연산 경로 추가
    visited[x] = 1 # 핵심2: 초깃값 방문 체크

    while q:
        x, path = q.popleft()
        path = path + [x] # 핵심3: 현재 값을 경로에 추가

        if x == 1: # 1에 도달하면 연산 횟수와 경로 반환
            return len(path) - 1, path
        if x % 3 == 0 and visited[x // 3] == 0:
            visited[x // 3] = 1
            q.append([x // 3, path])
        if x % 2 == 0 and visited[x // 2] == 0:
            visited[x // 2] = 1
            q.append([x // 2, path]) 
        if x - 1 > 0 and visited[x - 1] == 0:
            visited[x - 1] = 1
            q.append([x - 1, path])
    
step, path = bfs(n)
print(step)
print(*path)
