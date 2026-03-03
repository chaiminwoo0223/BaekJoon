# 열혈강호
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
result = [[]] + [list(map(int, input().split()))[1:] for _ in range(n)]
visited = [0] * (m + 1)
cnt = 0

def dfs(x):
    for i in result[x]:
        if check[i]:
            continue

        check[i] = 1

        if not visited[i] or dfs(visited[i]):
            visited[i] = x
            return 1 # 매칭

    return 0 # 매칭 X

for i in range(1, n+1):
    check = [0] * (m+1)

    if dfs(i):
        cnt += 1

print(cnt)
