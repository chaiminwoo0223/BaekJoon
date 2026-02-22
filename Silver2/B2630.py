# 색종이 만들기
# DFS
# 재귀
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
result = [0, 0] # 하얀색, 파란색

def dfs(x, y, n):
    paper = graph[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper != graph[i][j]:
                dfs(x, y, n // 2)
                dfs(x + n // 2, y, n // 2)
                dfs(x, y + n // 2, n // 2)
                dfs(x + n // 2, y + n // 2, n // 2)
                return

    result[paper] += 1

dfs(0, 0, n)

print(result[0])
print(result[1])
