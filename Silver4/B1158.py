# 요세푸스 문제
# 핵심: 원형으로 이루어진 큐를 생각하여 문제를 푸는 것
from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
deq = deque(range(1, n+1))
result = []

while deq:
    for i in range(k):
        deq.append(deq.popleft()) 
    result.append(deq.pop())

print(str(result).replace('[', '<').replace(']', '>'))
