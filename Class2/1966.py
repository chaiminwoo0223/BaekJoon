# 프린터 큐
from collections import deque

N = int(input())
for i in range(N):
    n, m = map(int, input().split())
    q = deque(list(map(int, input().split())))
    for j in range(n):
        print(j+1)