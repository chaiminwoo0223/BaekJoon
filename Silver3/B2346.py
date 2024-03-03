# 풍선 터뜨리기
from sys import stdin
from collections import deque

n = int(stdin.readline())
papers = list(map(int, stdin.readline().split()))
balloons = deque([(i + 1, papers[i]) for i in range(n)])
result = []

while balloons:
    idx, step = balloons.popleft()
    result.append(idx)
    if step > 0:
        balloons.rotate(-(step - 1))
    else:
        balloons.rotate(-step)

print(" ".join(map(str, result)))