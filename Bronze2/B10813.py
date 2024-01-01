# 공 바꾸기
import sys

N, M = map(int, sys.stdin.readline().split())
basket = [(n+1) for n in range(N)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1] # swap
print(' '.join(str(e) for e in basket))