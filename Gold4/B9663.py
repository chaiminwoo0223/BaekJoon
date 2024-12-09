# N-Queen
# PyPy3
# 2차원 리스트를 사용하지 않음
import sys

n = int(sys.stdin.readline())
board = [0] * n # 각 행에 배치된 퀸의 열 위치
count = 0 # 경우의 수

# x 행에 퀸 배치
def dfs(x):
    global count

    if x == n: # n개를 다 놓았다면 종료
        count += 1
        return
    
    for y in range(n): # 각 열에 퀸을 배치
        board[x] = y # x행 y열에 퀸을 배치
        if check(x):
            dfs(x+1)

# 현재 위치에 퀸을 배치할 수 있는지를 확인
def check(x):
    for i in range(x): # 이전 행들(i)과 현재 행(x)을 비교
        if board[x] == board[i]: # 같은 열에 퀸이 있는지를 확인
            return False # 배치 불가능
        if abs(x-i) == abs(board[x]-board[i]): # 대각선에 퀸이 있는지를 확인(두 퀸의 행 차이와 열 차이가 같으면 성립)
            return False # 배치 불가능
    return True # 배치 가능

dfs(0)
print(count)
