# 바구니 뒤집기
import sys

n, m = map(int, sys.stdin.readline().split())
basket = list(range(1, n+1))

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    basket = basket[:i-1] + list(reversed(basket[i-1:j])) + basket[j:]
print(' '.join(str(e) for e in basket))