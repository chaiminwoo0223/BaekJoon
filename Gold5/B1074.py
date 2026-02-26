# Z
import sys

input = sys.stdin.readline

n, r, c = map(int, input().split())
dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]
cnt = 0

def dfs(x, y, m):
    global cnt

    if x > r or x+m <= r or y > c or y+m <= c: # 핵심
        cnt += m**2
        return
    elif m > 2:
        dfs(x, y, m // 2)
        dfs(x, y + m // 2, m // 2)
        dfs(x + m // 2, y, m // 2)
        dfs(x + m // 2, y + m // 2, m // 2)
    else:
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if tx == r and ty == c:
                print(cnt + i)

dfs(0, 0, 2**n)
