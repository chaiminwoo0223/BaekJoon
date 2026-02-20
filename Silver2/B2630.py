# 색종이 만들기
# DFS
# 분할 정복 : 재귀적으로 자신을 호출하면서, 그 연산의 단위를 조금씩 줄여가는 방식
# 재귀
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
result = [0, 0] # 파란색, 흰색

def dfs(x, y, n):
    paper = graph[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper != graph[i][j]: # 핵심
                dfs(x, y, n // 2)
                dfs(x + n // 2, y, n // 2)
                dfs(x, y + n // 2, n // 2)
                dfs(x + n // 2, y + n // 2, n // 2)
                return

    result[paper] += 1

dfs(0, 0, n)

print(result[0])
print(result[1])
