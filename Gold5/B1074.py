# Z
import sys

n, r, c = map(int, sys.stdin.readline().split())
count = 0

def dfs(m, x, y):
    global count

    if x > r or x+m <= r or y > c or y+m <= c:
        count += m**2
        return
    elif m > 2:
        dfs(m // 2, x, y)
        dfs(m // 2, x, y + m // 2)
        dfs(m // 2, x + m // 2, y)
        dfs(m // 2, x + m // 2, y + m // 2)
    else:
        if x == r and y == c:
            print(count)
        elif x == r and y+1 == c:
            print(count + 1)
        elif x+1 == r and y == c:
            print(count + 2)
        else:
            print(count + 3)

dfs(2**n, 0, 0)
