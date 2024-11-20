# 주유소
import sys

n = int(sys.stdin.readline())
distance = list(map(int, sys.stdin.readline().split()))
oil = list(map(int, sys.stdin.readline().split()))
min_oil = oil[0] # 첫번째 주유소 가격
cost = 0

for i in range(n-1):
    if oil[i] < min_oil:
        min_oil = oil[i]
    cost += min_oil * distance[i]
print(cost)
