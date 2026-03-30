# Z
# 분할정복
import sys

input = sys.stdin.readline

n, r, c = map(int, input().split())
cnt = 0

def dfs(x, y, z):
    global cnt

    if not (x <= r < x + z and y <= c < y + z): # 핵심
        cnt += z * z
        return
    elif z > 2:
        t = z // 2

        dfs(x, y, t)
        dfs(x, y + t, t)
        dfs(x + t, y, t)
        dfs(x + t, y + t, t)
    else:
        for i in range(x, x+2):
            for j in range(y, y+2):
                if i == r and j == c:
                    print(cnt)
                    return
                else:
                    cnt += 1

dfs(0, 0, 2**n)
