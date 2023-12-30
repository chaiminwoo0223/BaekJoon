# 요세푸스 문제
from collections import deque
n, k = map(int, input().split())
result = []
queue = deque(range(1, n+1))

while queue:
    for i in range(k-1):
        queue.append(queue.popleft()) # 핵심
    result.append(queue.popleft())
print(str(result).replace('[', '<').replace(']', '>'))