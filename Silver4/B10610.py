# 30
import sys

n = sorted(sys.stdin.readline().rstrip(), reverse=True)

if '0' not in n or sum(map(int, n)) % 3 != 0:
    print(-1)
else:
    print("".join(n))
