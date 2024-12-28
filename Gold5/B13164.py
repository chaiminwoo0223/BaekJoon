# 행복 유치원
# 칸막이
import sys

n, k = map(int, sys.stdin.readline().split())
children = list(map(int, sys.stdin.readline().split()))
cost = sorted([children[i+1] - children[i] for i in range(n-1)], reverse=True)

print(sum(cost[k-1:]))
