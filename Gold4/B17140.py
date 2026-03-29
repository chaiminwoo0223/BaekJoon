# 이차원 배열과 연산
from collections import Counter
import sys

input = sys.stdin.readline

def calculator(a):
    n = len(a)
    m = len(a[0])

    if n <= m: # R 연산
        graph = []

        for i in range(n):
            x = []

            for c in sorted(Counter(a[i][j] for j in range(m) if a[i][j] != 0).most_common(), key=lambda x: (x[1], -x[0])):
                x += list(c)

            graph.append(x + [0] * (2 * m - len(x)))

    else: # S 연산
        graph = [[] for _ in range(2 * n)]

        for j in range(m):
            for r in sorted(Counter(a[i][j] for i in range(n) if a[i][j] != 0).most_common(), key=lambda x: (x[1], -x[0])):
                r += [0] * (2 * n - len(r))

                for i in range(n):
                    graph[2 * i] = r[0][0]
                    graph[2 * i + 1] = r[0][1]

    print(graph)

    return graph[:100][:100]

r, c, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(3)]
cnt = 0

while cnt <= 100:
    if a[r-1][c-1] == k:
        print(cnt)
        break
    else:
        cnt += 1
        a = calculator(a)

else:
    print(-1)
