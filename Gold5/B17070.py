# 파이프 옮기기 1
import sys
sys.setrecursionlimit(1000000)

n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[[-1] * 3 for _ in range(n)] for _ in range(n)] # DP 배열 초기화: dp[x][y][c]

def case1(x, y, c):
    if y+1 < n and board[x][y+1] == 0:
        dp[x][y][c] += dfs(x, y+1, 0)

def case2(x, y, c):
    if x+1 < n and board[x+1][y] == 0:
        dp[x][y][c] += dfs(x+1, y, 1)

def case3(x, y, c):
    if x+1 < n and y+1 < n and board[x+1][y] == 0 and board[x][y+1] == 0 and board[x+1][y+1] == 0:
        dp[x][y][c] += dfs(x+1, y+1, 2)

def dfs(x, y, c):
    if x == n-1 and y == n-1: # 도착 지점 도달 시 1 반환
        return 1
    elif dp[x][y][c] != -1: # 이미 계산된 경우
        return dp[x][y][c]
    else: # 초기화
        dp[x][y][c] = 0 
    
    if c == 0: # 가로
        case1(x, y, c)
        case3(x, y, c)
    elif c == 1: # 세로
        case2(x, y, c)
        case3(x, y, c)
    else: # 대각선
        case1(x, y, c)
        case2(x, y, c)
        case3(x, y, c)

    return dp[x][y][c]

print(dfs(0, 1, 0))
