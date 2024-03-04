# queuestack
from sys import stdin
from collections import deque

# 입력 처리
N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
B = list(map(int, stdin.readline().split()))
M = int(stdin.readline())
C = list(map(int, stdin.readline().split()))
queuestack = deque()

for i in range(N):
    if A[i] == 0:
        queuestack.appendleft(B[i])
        
for j in range(M):
    queuestack.append(C[j])
    print(queuestack.popleft(), end=' ')