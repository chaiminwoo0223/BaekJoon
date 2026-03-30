# 종이의 개수
import sys

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

result = {-1:0, 0:0, 1:0}

def dfs(x, y, z):
    t = graph[x][y] # 기준

    for i in range(x, x + z):
        for j in range(y, y + z):
            if graph[i][j] != t: # 종이 종류가 다르다면
                s = z // 3 # 종이 1/3로 분할

                dfs(x, y, s)
                dfs(x, y + s, s)
                dfs(x, y + 2 * s, s)
                dfs(x + s, y, s)
                dfs(x + s, y + s, s)
                dfs(x + s, y + 2 * s, s)
                dfs(x + 2 * s, y, s)
                dfs(x + 2 * s, y + s, s)
                dfs(x + 2 * s, y + 2 * s, s)

                return

    result[t] += 1

dfs(0, 0, n)

for r in result.values():
    print(r)
