# 스네이크버드
import sys

n, l = map(int, sys.stdin.readline().split())
heights = sorted(map(int, sys.stdin.readline().split()))

for height in heights:
    if height <= l:
        l += 1
print(l)
