# 종이의 개수
import sys

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
result = {-1:0, 0:0, 1:0}

def dfs(x, y, z):
    s = graph[x][y]
    t = z // 3

    for i in range(x, x+z):
        for j in range(y, y+z):
            if graph[i][j] != s:
                dfs(x, y, t)
                dfs(x, y + t, t)
                dfs(x, y + 2 * t, t)
                dfs(x + t, y, t)
                dfs(x + t, y + t, t)
                dfs(x + t, y + 2 * t, t)
                dfs(x + 2 * t, y, t)
                dfs(x + 2 * t, y + t, t)
                dfs(x + 2 * t, y + 2 * t, t)

                return

    result[s] += 1

dfs(0, 0, n)

for value in result.values():
    print(value)
