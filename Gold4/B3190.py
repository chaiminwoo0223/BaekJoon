# 뱀
from collections import deque
import sys

n = int(sys.stdin.readline()) # 보드의 크기
k = int(sys.stdin.readline()) # 사과 개수
board = [[0] * (n+1) for _ in range(n+1)] # 비어있으면 0, 사과이면 1, 뱀의 일부이면 2
move = deque([])

for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    board[a][b] = 1

l = int(sys.stdin.readline())

for _ in range(l):
    x, c = sys.stdin.readline().rstrip().split()
    move.append((int(x), c))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
snake = deque([(1, 1)]) # 뱀이 위치한 모든 좌표가 들어있다.
direction = 0 # 방향을 정의한 변수
time = 0 # 몇 초
x = 1
y = 1
board[1][1] = 2 # 뱀의 시작은 (1, 1)

def rotate(direction, c):
    if c == 'L': # 왼쪽으로 회전
        return (direction - 1) % 4
    if c == 'D': # 오른쪽으로 회전
        return (direction + 1) % 4

while True:
    x += dx[direction]
    y += dy[direction]

    if x >= 1 and x <= n and y >= 1 and y <= n and board[x][y] != 2: # x, y가 벽 또는 뱀의 몸이 아닐 때
        if board[x][y] == 1: # 사과가 있을 때
            board[x][y] = 2 # 사과를 없애고 뱀의 머리가 이동하며, 꼬리는 움직이지 않는다.
        else: # 사과가 없을 때
            board[x][y] = 2
            tx, ty = snake.popleft()
            board[tx][ty] = 0 # 꼬리가 위치한 칸을 비운다.
        snake.append((x, y))
        time += 1 # 1초 증가
        if move and time == move[0][0]: # 회전할 시간이라면
            direction = rotate(direction, move[0][1])
            move.popleft()
    else:
        time += 1
        break

print(time)
