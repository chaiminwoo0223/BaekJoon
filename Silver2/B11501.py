# 주식
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    score = list(map(int, sys.stdin.readline().split()))
    max_score = score[-1]
    count = 0

    for i in range(n-2, -1, -1):
        if score[i] >= max_score:
            max_score = score[i]
        else:
            count += (max_score - score[i])
    print(count)
