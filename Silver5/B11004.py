# K번째 수
import sys

n, k = map(int, sys.stdin.readline().split())
print(sorted(map(int, sys.stdin.readline().split()))[k-1])
