# 치킨 배달
from itertools import combinations
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
home = []
chicken = []
result = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home.append([i, j])
        if graph[i][j] == 2:
            chicken.append([i, j])

combination = combinations(chicken, m)

def calculator(c):
    visited = [[0] * n for _ in range(n)]
    number = 0

    for x, y in c:
        for v, w in home:
            difference = abs(x - v) + abs(y - w)
            if visited[v][w] == 0:
                visited[v][w] = difference
            else:
                visited[v][w] = min(visited[v][w], difference)
    
    for i in range(n):
        number += sum(visited[i])
    result.append(number)
        

for c in combination:
    calculator(c)

print(min(result))
