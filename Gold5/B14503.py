# 로봇 청소기
# 반시계 방향으로 90도 회전 = 왼쪽으로 90도 회전
# 3.1로 돌아간다.
from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dr = [-1, 0, 1, 0] 
dc = [0, 1, 0, -1]
q = deque([(r, c, d)])
count = 0

def rotate(d):
    return (d - 1) % 4 # 0 -> 3 -> 2 -> 1
    
def back(r, c, d):
    return r - dr[d], c - dc[d]

def bfs():
    global count
    while q:
        r, c, d = q.popleft()
        cleaned = False # 청소 여부 확인

        # 1번
        if graph[r][c] == 0:
            graph[r][c] = 2
            count += 1

        # 3번
        for _ in range(4): # 핵심: 3.3에서 "1번으로 돌아간다"는 "3.1로 돌아간다"는 뜻이다.
            d = rotate(d)
            tr, tc = r + dr[d], c + dc[d]
            if 0 <= tr < n and 0 <= tc < m and graph[tr][tc] == 0:
                q.append((tr, tc, d))
                cleaned = True
                break

        # 2번
        if not cleaned: # 현재 칸의 주변 4칸이 전부 청소되었다면
            tr, tc = back(r, c, d)
            if 0 <= tr < n and 0 <= tc < m:
                if graph[tr][tc] != 1: # 바라보는 방향을 유지하며 1칸 후진할 수 있다면
                    q.append((tr, tc, d)) # 후진
                else:
                    break # 종료
                    
bfs()

print(count)
