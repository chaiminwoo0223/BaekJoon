# 색종이 만들기
# 분할 정복 : 재귀적으로 자신을 호출하면서, 그 연산의 단위를 조금씩 줄여가는 방식
import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
numbers = [0, 0]

def dfs(x, y, n):
    color = graph[x][y] # 핵심

    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != graph[i][j]:
                dfs(x, y, n // 2)
                dfs(x, y + n // 2, n // 2)
                dfs(x + n // 2, y, n // 2)
                dfs(x + n // 2, y + n // 2, n // 2)
                return
    
    numbers[color] += 1

dfs(0, 0, n)
print(numbers[0])
print(numbers[1])
