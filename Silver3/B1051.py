# 숫자 정사각형
import sys

n, m = map(int, sys.stdin.readline().split())
box = [[] for _ in range(n)]
t = 1
minimum = min(n, m)
result = []

for i in range(n):
    for number in sys.stdin.readline().rstrip():
        box[i].append(number)

def check(x, y):
    global t
    while t < minimum and 0 <= x + t < n and 0 <= y + t < m:
        if box[x][y] == box[x + t][y] and box[x + t][y] == box[x][y + t] and box[x][y] == box[x + t][y + t]:
            result.append(t + 1)
        t += 1
    t = 1
    
for i in range(n-1):
    for j in range(m-1):
        check(i, j)

if result:
    print(max(result)**2)
else:
    print(1)
