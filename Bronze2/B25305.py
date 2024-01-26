# 커트라인
import sys

n, k = map(int, sys.stdin.readline().split())
X = list(map(int, sys.stdin.readline().split()))

print(sorted(X)[n-k])