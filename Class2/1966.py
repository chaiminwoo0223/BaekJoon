# 프린터 큐
# 나의 숫자가 남은 큐 중에서 가장 큰 수가 될 때까지 검사
from collections import deque

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    q = deque(list(map(int, input().split())))
    cnt = 0
    while True: # 핵심1
        best = max(q)
        front = q.popleft()
        m -= 1
        if best == front:
            cnt += 1
            if m < 0:
                print(cnt)
                break
        else:
            q.append(front)
            if m < 0: # 핵심2
                m = len(q)-1