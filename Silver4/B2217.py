# 로프
import sys

n = int(sys.stdin.readline())
w = sorted([int(sys.stdin.readline()) for _ in range(n)], reverse=True)
result = [w[i] * (i+1) for i in range(n)]

print(max(result))
